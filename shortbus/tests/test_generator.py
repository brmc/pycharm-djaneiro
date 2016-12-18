#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from unittest import TestCase
from xml.etree import ElementTree

import collections

from ..templategenerator import SnippetGenerator, TemplateDefinition, \
    VariableDefinition

try:
    from yaml import CLoader as Loader, CDumper as Dumper, dump
except ImportError:
    from yaml import Loader, Dumper


class GeneratorTest(TestCase):
    def setUp(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.valid_yml_path = os.path.join(
            self.directory, 'yml', 'valid.yml')
        self.warning_yml_path = os.path.join(
            self.directory, 'yml', 'warns.yml')
        self.jetbrains_xml = os.path.join(
            self.directory, 'yml', 'jetbrains.xml')

        self.sublime_xml = os.path.join(self.directory, 'yml')

        self.generator = SnippetGenerator('Djaneiro: Models').import_from_yml(self.valid_yml_path)

        self.yml_templates = SnippetGenerator().import_from_yml(
            self.valid_yml_path).yml_templates

        self.xml_templates = SnippetGenerator().import_from_jetbrains_format(
            self.jetbrains_xml).jetbrains_templates

    def test_default_values_for_template_and_raw(self):
        variables = {
            'var': VariableDefinition('var'),
            'end': VariableDefinition('end')
        }

        value = '$var$ = models.AutoField($var$)$end$'
        default = TemplateDefinition(
            name='raw',
            value=value,
            variables=variables,
        )

        template = self.yml_templates['raw']

        self.assertEqual(default, template)

        value = '$moo$\n$joo$'

        variables = {
            'moo': VariableDefinition('moo'),
            'joo': VariableDefinition('joo')
        }

        default.value = value
        default.variables = variables
        default.name = 'template'

        template = self.yml_templates['template']

        self.assertEqual(default, template)

    def test_variable_default_definitions(self):
        value = '$weep$ $graa:nah$ $weep:$ $:ni$ $ni$ $$'

        template = self.yml_templates['bah']
        variables = template.variables

        self.assertEqual(variables['weep'].defaultValue, 'suckit')
        self.assertEqual(variables['graa'].defaultValue, 'hard')
        self.assertEqual(variables['VAR3'].defaultValue, 'ni')
        self.assertEqual(variables['ni'].defaultValue, '')

        self.assertEqual(template.value, '$weep$ $graa$ $weep$ $VAR3$ $ni$ $$')
        self.assertEqual(len(variables), 4)


    def test_variable_typo_throws_warning(self):
        with self.assertWarns(Warning):
            SnippetGenerator().import_from_yml(self.warning_yml_path)

    def test_create_from_jetbrains_format(self):
        tpl = self.xml_templates['mauto']

        variables = {
            'VAR': VariableDefinition(name='VAR', defaultValue='FIELDNAME'),
            'VAR2': VariableDefinition(name='VAR2')
        }

        template = TemplateDefinition(
            name='mauto',
            value='$VAR$ = models.AutoField($VAR2$)',
            toReformat=False,
            toShortenFQNames=True,
            variables=variables
        )

        self.assertEqual(tpl, template)

    def test_jetbrains_export(self):
        group = 'Djaneiro: Models'
        a = TemplateDefinition(
            name='mauto',
            value='$VAR$ = models.AutoField($VAR2$)',
            toReformat=False,
            toShortenFQNames=True,
            variables={
                'VAR': VariableDefinition('VAR', 'FIELDNAME'),
                'VAR2': VariableDefinition('VAR2')
            }
        )

        generator = SnippetGenerator(group)
        generator.yml_templates = {'mauto': a}

        generator.merge_all_templates()
        a = generator.export_to_jetbrains('bullshit.xml')
        b = ElementTree.parse(self.jetbrains_xml).getroot()

        self.assertEqual(a.tag, b.tag)
        template_a, template_b = a.findall('template')[0], b.findall('template')[0]
        self.assertEqual(sorted(template_a.items()) , sorted(template_b.items()))

        variables_a = template_a.findall('variable')
        variables_b = template_b.findall('variable')
        variables = zip(variables_a, variables_b)

        for a, b in variables:
            self.assertEqual(sorted(a.items()),
                             sorted(b.items()))

        options_a = template_a.find('context').findall('option')
        options_b = template_b.find('context').findall('option')

        options = zip(options_a, options_b)
        for a, b in options:
            self.assertEqual(sorted(a.items()),
                             sorted(b.items()))

    def test_import_from_sublime(self):
        a = SnippetGenerator('test')
        path = '/home/brian/dev/jetbrains/pycharm-djaneiro/sublime/Models'
        obj = a.import_from_sublime_format(path)

        obj.merge_all_templates()
        obj.export_to_jetbrains('monkey.xml')
        obj.export_to_yml('stupid.yml')
        self.assertEqual("a", obj.sublime_templates['mauto'].value)

