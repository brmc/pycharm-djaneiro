#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import warnings
from sys import argv

from shortbus.transpiler import Transpiler

if __name__ == '__main__':
    jb_root = os.path.join('plugin', 'resources', 'liveTemplates')
    jb_file = 'Djaneiro_{}.xml'
    yml_file = '{}.yml'
    group_format = 'Djaneiro: {}'
    sub_root = 'sublime'
    mod_root = 'modifications'

    groups = {
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
        }
    }

    output_path = os.path.join(mod_root, 'output')
    yml_output_path = os.path.join(output_path, 'yml')

    if len(argv[1:]) == 0 or 'all' in argv[2:]:
        argv += groups.keys()

    for arg in argv[1:]:
        if arg == 'all':
            continue
        if arg.lower().startswith('custom='):
            path = arg.split('=')[-1]
            file = os.path.split(path)[-1]
            name = file.split('.')[0]
            output_file = os.path.join(
                output_path, jb_file.format(name.capitalize()))

            template_group = group_format.format(name)
            transpiler = Transpiler(template_group)
            transpiler.import_from_yml(path)
            transpiler.merge_all_templates()
            transpiler.export_to_jetbrains(output_file)

            continue

        paths = groups.get(arg, {})
        print(paths)

        if paths == {}:
            warnings.warn('Invalid parameter: {}.  Must be Forms, Models, '
                          'Views, Python, or Templates. skipping...'.format(arg))
            continue

        template_group = group_format.format(arg)
        output_file = os.path.join(output_path, jb_file.format(arg))
        yml_output_file = os.path.join(yml_output_path, yml_file.format(arg))
        transpiler = Transpiler(template_group)

        for type, path in paths.items():
            if type == 'jetbrains':
                transpiler.import_from_jetbrains_format(path)
            elif type == 'sublime':
                transpiler.import_from_sublime_format(path)
            elif type == 'modifications':
                transpiler.import_from_yml(path)

        transpiler.merge_all_templates()
        transpiler.export_to_jetbrains(output_file).export_to_yml(yml_output_file)

