#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import re
import warnings
from collections import OrderedDict
from functools import wraps
from xml import etree


def warn_if_missing_templates(func):
    @wraps(func)
    def method(self, *method_args, **method_kwargs):
        if self.templates == {}:
            raise KeyError(
                "You seem to be missing some templates.  If you've already "
                "imported templates,"
                "then you need to merge them `merge_all_templates()`")

        func(self, *method_args, **method_kwargs)

    return method


class ContextDefinition(object):
    def __init__(self, name='Python', value=True):
        self.name: str = name
        self.value: bool = value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def to_jetbrains_dict(self):
        return {
            'name': self.name,
            'value': str(self.value).lower()
        }


class VariableDefinition(object):
    def __init__(self, name, defaultValue='', expression='',
                 alwaysStopAt=True):
        self.name: str = name
        self.defaultValue: str = defaultValue.strip('"\'')
        self.expression: str = expression
        self.alwaysStopAt: bool = alwaysStopAt

    def __eq__(self, other):
        return self.name == other.name \
               and self.expression == other.expression \
               and self.defaultValue == other.defaultValue \
               and self.alwaysStopAt is other.alwaysStopAt

    def to_jetbrains_dict(self):
        return {
            'name': self.name,
            'expression': self.expression,
            'defaultValue': f'"{self.defaultValue}"',

            'alwaysStopAt': str(self.alwaysStopAt).lower()
        }


class TemplateDefinition(object):
    variable_prefix: str = 'VAR{}'
    VARIABLE_WRAPPER: str = '${}$'
    VARIABLE_REGEX = r'(?P<raw>\$(?P<variable>[\w_\.]*)?:?(?P<default>[^\$]*)?\$)'
    SUBLIME_CONTENT_REGEX = r'\<\!\[CDATA\[(.*)\]\]'
    SUBLIME_VARIABLE_REGEX = r'(?P<raw>\$\{?(?P<variable>\d):?(?P<default>[\w_\s]*)\}?)'

    def __init__(
            self,
            name,
            value='',
            variables=None,
            context_options=None,
            shortcut='TAB',
            description='',
            toReformat=True,
            toShortenFQNames=True):

        self.name = name
        self.value = value
        self.shortcut = shortcut
        self.description = description

        self.toReformat = toReformat
        self.toShortenFQNames = toShortenFQNames

        self.variables = variables or {}
        self.context_options = context_options or [ContextDefinition()]

    def __eq__(self, other):
        equals = [
            'name',
            'value',
            'variables',
            'context_options',
            'shortcut',
            'description'
        ]

        for item in equals:
            if getattr(self, item) != getattr(other, item):
                return False

        same = ['toReformat', 'toShortenFQNames']

        for item in same:
            if getattr(self, item) is not getattr(other, item):
                return False

        return True

    def format_description_lazily(self):
        name = self.value.split('.')[0].split('(')[0]
        self.description = f"{name} ({self.value})"

    def to_jetbrains_dict(self):
        return {
            'name': self.name,
            'value': self.value,
            'toReformat': str(self.toReformat).lower(),
            'toShortenFQNames': str(self.toShortenFQNames).lower()
        }

    def to_yml_dict(self):
        return {
            'name': self.name,
            'raw': self.value,
            'toReformat': self.toReformat,
            'toShortenFQNames': self.toShortenFQNames,
            'variables': [var.__dict__ for var in self.variables.values()],
            'context': [options.__dict__ for options in self.context_options],
            'shortcut': self.shortcut,
            'description': self.description
        }

    @staticmethod
    def build_from_yml(yml: {}):
        """
        :param yml:
        :return:
        """
        try:
            name = yml.pop('name')
        except KeyError:
            msg = "your template needs a name. you should fix that, corndog"
            raise KeyError(msg)

        value = yml.pop('raw', None)

        if value is None:
            try:
                path = yml.pop('template')

                with open(path) as file:
                    value = file.read()

            except KeyError as _:
                msg = "Your stupid yml file is broke.  entry needs either a " \
                      "raw or template field. fix it!\n"
                raise KeyError(msg)
            except FileNotFoundError as _:
                raise FileNotFoundError('Aint no file. get out')

        context = yml.pop('context', [{}])
        context_options = [ContextDefinition(**x) for x in context]

        value, variables = parse_and_extract_variables(
            value, TemplateDefinition.VARIABLE_REGEX)

        for i, variable in enumerate(yml.pop('variables', [])):
            variable_name = variable.get('name')

            if variable_name not in variables.keys():
                message = "Variable '{variable_name}' not found in '{name}': " \
                          "{value}. Skipping..."
                warnings.warn(message)
                continue

            variables[variable_name] = VariableDefinition(**variable)

        return TemplateDefinition(
            name=name,
            value=value,
            context_options=context_options,
            variables=variables,
            **yml)

    @staticmethod
    def build_from_xml(xml: {}):
        attrs = xml.attrib
        name = attrs['name']
        raw_vars = xml.findall('variable')

        toReformat = attrs['toReformat'].lower()
        toShortenFQNames = attrs['toShortenFQNames'].lower()

        boolean_converter = {
            'true': True,
            'false': False
        }

        toReformat = boolean_converter[toReformat]
        toShortenFQNames = boolean_converter[toShortenFQNames]

        variables = [VariableDefinition(**var.attrib) for var in raw_vars]

        variables = {var.name: var for var in variables}

        context = xml.find('context')
        options = []

        for option in context.findall('option'):
            option_name = option.attrib['name']
            value = option.attrib['value'].lower()
            value = boolean_converter[value]

            options.append(ContextDefinition(name=option_name, value=value))

        return TemplateDefinition(
            name,
            value=attrs['value'],
            toReformat=toReformat,
            toShortenFQNames=toShortenFQNames,
            variables=variables,
            context_options=options
        )

    @staticmethod
    def build_from_snippet(xml: etree):
        name = xml.findtext('tabTrigger')
        content = xml.findtext('content')

        value, variables = parse_and_extract_variables(
            content, TemplateDefinition.SUBLIME_VARIABLE_REGEX)

        scope = xml.findtext('scope')
        context = ContextDefinition(scope.split('.')[-1].capitalize())

        description = xml.findtext('description')

        return TemplateDefinition(
            name=name,
            value=value,
            description=description,
            variables=variables,
            context_options=[context])


def parse_and_extract_variables(string: str, regex: str, variables=None):
    pattern = re.compile(regex)
    string = string.replace("$:$", "$$")
    format_variable = TemplateDefinition.variable_prefix.format
    wrap_variable = TemplateDefinition.VARIABLE_WRAPPER.format

    matches = pattern.findall(string)
    variables = variables or OrderedDict()

    for i, match in enumerate(matches):
        raw_match, variable_name, default_value = match

        max_replace = 1 if variable_name == '' else -1

        if variable_name == '':
            variable_name = format_variable(i + 1)
        elif variable_name.isdigit():
            var = int(variable_name)
            variable_name = format_variable(var)

        variable_dict = VariableDefinition(
            name=variable_name,
            defaultValue=default_value)

        variables[variable_name] = variable_dict
        variable_name = wrap_variable(variable_name)
        string = string.replace(raw_match, variable_name, max_replace)

    return string, variables