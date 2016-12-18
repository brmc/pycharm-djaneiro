#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from shortbus.transpiler import Transpiler

if __name__ == '__main__':
    jb_root = os.path.join('plugin', 'resources', 'liveTemplates')
    jb_file = 'Djaneiro_{}.xml'
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

    for group, paths in groups.items():
        template_group = group_format.format(group)
        output_file = os.path.join(output_path, jb_file.format(group))
        transpiler = Transpiler(template_group)

        for type, path in paths.items():
            if type == 'jetbrains':
                transpiler.import_from_jetbrains_format(path)
            elif type == 'sublime':
                transpiler.import_from_sublime_format(path)
            elif type == 'modifications':
                transpiler.import_from_yml(path)

        transpiler.merge_all_templates()
        transpiler.export_to_jetbrains(output_file)

