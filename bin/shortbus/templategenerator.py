#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import re
import warnings
#from lxml import etree as ElementTree
from lxml import etree as ElementTree


from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class ContextDefinition(object):
    def __init__(self, name='Python', value=True):
        self.name = name
        self.value = value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def to_jetbrains_dict(self):
        return {
            'name': self.name,
            'value': str(self.value).lower()
        }

class VariableDefinition(object):
    def __init__(self, name, default='', expression='', always_stop_at=True):
        self.name = name
        self.default = default
        self.expression = expression
        self.always_stop_at = always_stop_at

    def __eq__(self, other):
        return self.name == other.name \
               and self.expression == other.expression \
               and self.default == other.default \
               and self.always_stop_at is other.always_stop_at

    def to_jetbrains_dict(self):
        return {
            'name': self.name,
            'expression': self.expression,
            'defaultValue': '"{}"'.format(self.default) if self.default else '',
            'alwaysStopAt': str(self.always_stop_at).lower()
        }


class TemplateDefinition(object):
    variable_prefix = 'VAR{}'
    VARIABLE_REGEX = r'\$([\w_]*:?[\w_]*)\$'

    def __init__(
            self,
            name,
            expands_to='',
            variables=None,
            context_options=None,
            shortcut='TAB',
            description='',
            to_reformat=True,
            to_shorten_fq_names=True):

        self.name = name
        self.expands_to = expands_to
        self.shortcut = shortcut
        self.description = description

        self.to_reformat = to_reformat
        self.to_shorten_fq_names = to_shorten_fq_names

        self.variables = variables or {}
        self.context_options = context_options or [ContextDefinition()]

    def __eq__(self, other):
        equals = [
            'name',
            'expands_to',
            'variables',
            'context_options',
            'shortcut',
            'description'
        ]

        for item in equals:
            if getattr(self, item) != getattr(other, item):
                return False

        same = ['to_reformat', 'to_shorten_fq_names']

        for item in same:
            if getattr(self, item) is not getattr(other, item):
                return False

        return True

    def to_jetbrains_dict(self):
        return {
            'name': self.name,
            'value': self.expands_to,
            'toReformat': str(self.to_reformat).lower(),
            'toShortenFQNames': str(self.to_shorten_fq_names).lower()
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

        expands_to = yml.pop('raw', None)

        if expands_to is None:
            try:
                path = yml.pop('template')

                with open(path) as file:
                    expands_to = file.read()

            except KeyError as _:
                msg = "Your stupid yml file is broke.  entry needs either a " \
                      "raw or template field. fix it!\n"
                raise KeyError(msg)
            except FileNotFoundError as _:
                raise FileNotFoundError('Aint no file. get out')

        context = yml.pop('context', [{}])
        context_options = [ContextDefinition(**x) for x in context]

        pattern = re.compile(TemplateDefinition.VARIABLE_REGEX)
        matches = pattern.findall(expands_to)

        variables = {}

        for i, variable in enumerate(matches):
            if variable in ["", ":"]:
                continue

            variable_name, default_value = variable.partition(":")[::2]

            if not variable_name:
                variable_name = TemplateDefinition.variable_prefix.format(i)

            variable_dict = VariableDefinition(
                name=variable_name,
                default=default_value)

            variables[variable_name] = variable_dict
            expands_to = expands_to.replace(variable, variable_name)

        expands_to = expands_to.replace("$:$", "$$")

        for i, variable in enumerate(yml.pop('vars', [])):
            variable_name = variable.get('name')

            if variable_name not in variables.keys():
                message = "Variable '{}' not found in '{}': {}. Skipping..."
                warnings.warn(message.format(variable_name, name, expands_to))
                continue

            variables[variable_name] = VariableDefinition(**variable)


        return TemplateDefinition(
            name=name,
            expands_to=expands_to,
            context_options=context_options,
            variables=variables,
            **yml)

    @staticmethod
    def build_from_xml(xml: {}):
        attrs = xml.attrib
        name = attrs['name']
        raw_vars = xml.findall('variable')

        to_reformat = attrs['toReformat'].lower()
        to_shorten_fq_names = attrs['toShortenFQNames'].lower()

        boolean_converter = {
            'true': True,
            'false': False
        }

        to_reformat = boolean_converter[to_reformat]
        to_shorten_fq_names = boolean_converter[to_shorten_fq_names]

        variables = [VariableDefinition(
            name=var.attrib['name'],
            default=var.attrib['defaultValue'].replace('"', ''),
            expression=var.attrib['expression']
        ) for var in raw_vars]

        variables = {var.name: var for var in variables}

        context = xml.findall('context')[0]
        options = []

        for option in context.findall('option'):
            option_name = option.attrib['name']
            value = option.attrib['value'].lower()
            value = boolean_converter[value]

            options.append(ContextDefinition(name=option_name, value=value))

        return TemplateDefinition(
            name,
            expands_to=attrs['value'],
            to_reformat=to_reformat,
            to_shorten_fq_names=to_shorten_fq_names,
            variables=variables,
            context_options=options
        )


class SnippetGenerator(object):
    templates = {}

    def __init__(self, name="Template Group"):
        self.name = name
        self.jetbrains_templates = {}
        self.yml_templates = {}
        self.sublime_templates = {}

    def create_from_yml(self, path: str):
        """
        :param path:
        :return:
        """
        stream = open(path)
        data = load(stream, Loader=Loader)
        stream.close()

        templates = [TemplateDefinition.build_from_yml(x) for x in data]

        templates = {template.name: template for template in templates}

        self.yml_templates = templates

        return self

    def create_from_jetbrains_format(self, path):
        xml = ElementTree.parse(path).getroot()
        self.name = xml.attrib['group']

        templates = [TemplateDefinition.build_from_xml(child) for child in xml]
        templates = {template.name: template for template in templates}

        self.jetbrains_templates = templates

        return self

    def export_to_jetbrains(self, output_path):
        template_set = ElementTree.Element('templateSet')
        template_set.attrib['group'] = self.name

        for key, template in self.yml_templates.items():
            xml_template = ElementTree.SubElement(
                template_set,
                'template',
                template.to_jetbrains_dict())

            for key, var in template.variables.items():
                ElementTree.SubElement(
                    xml_template,
                    'variable',
                    var.to_jetbrains_dict())

            context = ElementTree.SubElement(xml_template, 'context')

            for option in template.context_options:
                ElementTree.SubElement(
                    context,
                    'option',
                    option.to_jetbrains_dict())

        tree = ElementTree.ElementTree(template_set)

        tree.write(output_path, pretty_print=True)
        return template_set

