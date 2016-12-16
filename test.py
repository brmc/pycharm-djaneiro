
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import sys

import re

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


path = '/home/brian/dev/jetbrains/pycharm-djaneiro/test.yml'
stream = open(path)
data = load(stream, Loader=Loader)


class ContextDefinition(object):
    def __init__(self, name='Python', value=True):
        self.name = name
        self.value = value

class AutoNameSetterMixin():
    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

class VariableDefinition(AutoNameSetterMixin, object):
    expression = ''
    default = ''
    always_stop_at = True

    def __init__(self, name, *args, **kwargs):
        self.name = name

        super(VariableDefinition, self).__init__(*args, **kwargs)

class TemplateDefinition(AutoNameSetterMixin, object):
    expands_to = ''
    variables = []

    context_options = [ContextDefinition()]

    shortcut = 'TAB'
    description = ''
    to_reformat = True
    to_shorten_fq_names = True

    def __init__(self, name, expands_to, *args, **kwargs):
        self.name = name
        self.expands_to = expands_to

        super(TemplateDefinition, self).__init__(*args, **kwargs)

class LiveTemplateGenerator(object):
    template = None

    variable_prefix = 'VAR{}'
    VARIABLE_REGEX = r'\$([\w_]*)\$'

    def __init__(self, template):
        self.template = template

    @staticmethod
    def create_from_yml(yml: {}):
        """
        :param yml:
        :return:
        """

        # intentionally not providing default value
        name = yml.pop('name')


        context = yml.pop('context', [])
        context_options = [ContextDefinition(**x) for x in context]

        expansion = yml.pop('raw', None)

        if expansion is None:
            try:
                path = yml.pop('template')

                with open(path) as file:
                    expansion = file.read()

            except KeyError as e:
                raise KeyError("Your stupid yml file is broke.  entry needs either a raw or template field. fix it!\n")
            except FileNotFoundError as e:
                raise FileNotFoundError('Aint no file. get out')

        # generator.expansion = expansion

        pattern = re.compile(LiveTemplateGenerator.VARIABLE_REGEX)
        matches = pattern.findall(expansion)

        vars = {}

        for i, variable in enumerate(yml.pop('vars', [])):
            vars[variable.get('name')] = VariableDefinition(**variable)

        if len(vars) < len(matches):
            for i, variable in enumerate(matches):
                if variable in vars.keys():
                    continue

                if variable == '':
                    name = LiveTemplateGenerator.variable_prefix.format(i)
                    default = ''
                else:
                    name = variable
                    default = variable

                variable_dict = VariableDefinition(name=name, default=default)
                vars[name] = (variable_dict)

        template = TemplateDefinition(
            name=name,
            expands_to=expansion,
            context_options=context_options,
            variables=vars,
            **yml)

        return LiveTemplateGenerator(template)


    def generate_jetbrains_format(self):
        pass


templates = [LiveTemplateGenerator.create_from_yml(d) for d in data]

print(templates)