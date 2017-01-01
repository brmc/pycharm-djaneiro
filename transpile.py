#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import warnings
from sys import argv

from shortbus.transpiler import Transpiler

print(argv)

if __name__ == '__main__':
    jb_root = os.path.join('plugin', 'resources', 'liveTemplates')
    jb_file = 'Djaneiro_{}.xml'
    yml_file = '{}.yml'
    group_format = 'Djaneiro: {}'
    sub_root = 'sublime'
    mod_root = 'modifications'
    output_path = os.path.join(mod_root, 'output')
    yml_output_path = os.path.join(output_path, 'yml')

    source = argv[1].lower()

    if source.lower().startswith('custom='):
        path = source.split('=')[-1]
        file = os.path.split(path)[-1]
        name = file.split('.')[0]
        output_file = os.path.join(
            output_path, jb_file.format(name.capitalize()))

        template_group = group_format.format(name)
        transpiler = Transpiler(template_group)
        transpiler.import_from_yml(path)
        transpiler.merge_all_templates()
        transpiler.export_to_jetbrains(output_file)


    all_sources = ['all', 'jetbrains', 'sublime', 'modifications']

    if not source.startswith('custom=') and source not in all_sources:
        raise Exception('{} is not a valid source.  The first parameter '
                        'should one of these: {}'.format(source, all_sources))

    sources = all_sources[1:] if source == 'all' else [source]

    targets = argv[2:]

    groups_for_source = {
        'all': ['Forms', 'Models', 'Python', 'Templates', 'Views'],
        'jetbrains': ['Completions', 'Forms', 'Models', 'Python', 'Templates', 'Views'],
        'sublime': ['Forms', 'Models', 'Python', 'Templates', 'Views'],
        'modifications': [
            'Completions',
            'Forms',
            'Models',
            'Python',
            'Templates',
            'Views',
            'Postgres',
            'Widgets'
            'Settings'
        ]
    }

    if targets == []:
        targets = groups_for_source[source]

    groups = {
        'Completions': {
            'jetbrains':   os.path.join(jb_root, jb_file.format('Completions')),
        },
        'Forms': {
            'jetbrains': os.path.join(jb_root, jb_file.format('Forms')),
            'sublime': os.path.join(sub_root, 'Forms'),
            'modifications': os.path.join(mod_root, 'Forms.yml')
        },
        'Models': {
            'jetbrains': os.path.join(jb_root, jb_file.format('Models')),
            'sublime': os.path.join(sub_root, 'Models'),
            'modifications': os.path.join(mod_root, 'Models.yml')
        },
        'Views': {
            'jetbrains': os.path.join(jb_root, jb_file.format('Views')),
            'sublime': os.path.join(sub_root, 'Views'),
            'modifications': os.path.join(mod_root, 'Views.yml')
        },
        'Python': {
            'jetbrains': os.path.join(jb_root, jb_file.format('Python')),
            'sublime': os.path.join(sub_root, 'python'),
            'modifications': os.path.join(mod_root, 'Python.yml')
        },
        'Templates': {
            'jetbrains': os.path.join(jb_root, jb_file.format('Templates')),
            'sublime': os.path.join(sub_root, 'html'),
            'modifications': os.path.join(mod_root, 'Templates.yml')
        },
        'Postgres': {
            'modifications': os.path.join(mod_root, 'Postgres.yml')
        },
        'Widgets': {
            'modifications': os.path.join(mod_root, 'Widgets.yml')
        },
        'Settings': {
            'modifications': os.path.join(mod_root, 'Settings.yml')
        }
    }

    for group in targets:
        if group.lower().startswith('custom='):
            path = group.split('=')[-1]
            file = os.path.split(path)[-1]
            name = file.split('.')[0]
            output_file = os.path.join(
                output_path, jb_file.format(name.capitalize()))

            template_group = group_format.format(name)
            transpiler = Transpiler(template_group)
            transpiler.import_from_yml(path)
            transpiler.merge_all_templates()
            transpiler.export_to_jetbrains(output_file)

            break

        paths = groups.get(group, {})

        if paths == {}:
            warnings.warn('Invalid parameter: {}.  Must be Forms, Models, '
                          'Views, Python, or Templates. skipping...'.format(group))
            continue

        template_group = group_format.format(group)
        output_file = os.path.join(output_path, jb_file.format(group))
        yml_output_file = os.path.join(yml_output_path, yml_file.format(group))
        transpiler = Transpiler(template_group)

        for source in sources:
            if source == 'jetbrains':
                transpiler.import_from_jetbrains_format(paths[source])
            elif source == 'sublime':
                transpiler.import_from_sublime_format(paths[source])
            elif source == 'modifications':
                transpiler.import_from_yml(paths[source])
                transpiler.merge_all_templates()
                transpiler.export_to_markdown(group, 'modifications/output/markdown')
                transpiler.export_abbreviations(group, 'modifications/output/abbreviations')

        transpiler.merge_all_templates()
        transpiler.export_to_jetbrains(output_file).export_to_yml(yml_output_file)

