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

        self.generator = SnippetGenerator('Djaneiro: Models').create_from_yml(self.valid_yml_path)

        self.yml_templates = SnippetGenerator().create_from_yml(
            self.valid_yml_path).yml_templates

        self.xml_templates = SnippetGenerator().create_from_jetbrains_format(
            self.jetbrains_xml).jetbrains_templates

    def test_default_values_for_template_and_raw(self):
        variables = {
            'var': VariableDefinition('var'),
            'end': VariableDefinition('end')
        }

        expands_to = '$var$ = models.AutoField($var$)$end$'
        default = TemplateDefinition(
            name='raw',
            expands_to=expands_to,
            variables=variables,
        )

        template = self.yml_templates['raw']

        self.assertEqual(default, template)

        expands_to = '$moo$\n$joo$'

        variables = {
            'moo': VariableDefinition('moo'),
            'joo': VariableDefinition('joo')
        }

        default.expands_to = expands_to
        default.variables = variables
        default.name = 'template'

        template = self.yml_templates['template']

        self.assertEqual(default, template)

    def test_variable_default_definitions(self):
        expands_to = '$weep$ $graa:nah$ $weep:$ $:ni$ $ni$ $$'

        template = self.yml_templates['bah']
        variables = template.variables

        self.assertEqual(variables['weep'].default, 'suckit')
        self.assertEqual(variables['graa'].default, 'hard')
        self.assertEqual(variables['VAR3'].default, 'ni')
        self.assertEqual(variables['ni'].default, '')

        self.assertEqual(len(variables), 4)

        self.assertEqual(template.expands_to, '$weep$ $graa$ $weep$ $VAR3$ $ni$ $$')

    def test_variable_typo_throws_warning(self):
        with self.assertWarns(Warning):
            SnippetGenerator().create_from_yml(self.warning_yml_path)

    def test_create_from_jetbrains_format(self):
        tpl = self.xml_templates['mauto']

        variables = {
            'VAR': VariableDefinition(name='VAR', default='FIELDNAME'),
            'VAR2': VariableDefinition(name='VAR2')
        }

        template = TemplateDefinition(
            name='mauto',
            expands_to='$VAR$ = models.AutoField($VAR2$)',
            to_reformat=False,
            to_shorten_fq_names=True,
            variables=variables
        )

        self.assertEqual(tpl, template)

    def test_jetbrains_export(self):
        group = 'Djaneiro: Models'
        a = TemplateDefinition(
            name='mauto',
            expands_to='$VAR$ = models.AutoField($VAR2$)',
            to_reformat=False,
            to_shorten_fq_names=True,
            variables={
                'VAR': VariableDefinition('VAR', 'FIELDNAME'),
                'VAR2': VariableDefinition('VAR2')
            }
        )

        generator = SnippetGenerator(group)
        generator.yml_templates = {'mauto': a}

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

        options_a = template_a.findall('context')[0].findall('option')
        options_b = template_b.findall('context')[0].findall('option')

        options = zip(options_a, options_b)
        for a, b in options:
            self.assertEqual(sorted(a.items()),
                             sorted(b.items()))



