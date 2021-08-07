import argparse
import os
import pathlib
from typing import Optional
from ppline.easy.command import Run



def _arg_project_dir(arg):
    expanded = os.path.expanduser(arg)
    if os.path.isdir(expanded):
        return os.path.abspath(os.path.normpath(expanded))
    else:
        raise Exception(f'Argument {arg} must be an existing directory.')

# def _arg_directory(arg):
#     expanded = os.path.expanduser(arg)
#     if os.path.isdir(expanded):
#         return os.path.abspath(os.path.normpath(expanded))
#     else:
#         raise Exception(f'Argument {arg} must be an existing directory.')

# def _arg_trigger_class(arg):
#     expanded = os.path.expanduser(arg)
#     if os.path.isdir(expanded):
#         return os.path.abspath(os.path.normpath(expanded))
#     else:
#         raise Exception(f'Argument {arg} must be an existing directory.')


def _arg_config_file(arg):
    if pathlib.Path(arg).suffix not in ['.yml', '.yaml']:
        raise Exception(f'Argument {arg} must be a .yml/.yaml file.')
    if os.path.exists(arg)==False:
        raise Exception(f'Cannot find {arg} at your directory')
    return arg


parser = argparse.ArgumentParser()
parser.add_argument('--trigger_class', '-tc', default=None, help='Path to class to trigger (in the form of "to/the/file.py:TestClass. TestClass should have a __call__ method").')
parser.add_argument('--project_dir', '-p', type=_arg_project_dir, default=None, help="Path to project's root where configuration .yml/.yaml file is stored.")
parser.add_argument('--config_file', '-f', type=_arg_config_file, default=None, help='Name of pipeline configuration .yml/.yaml file.')

# req_grp = parser.add_argument_group(title='Required')
# req_grp.add_argument('--config_file', type=_arg_config_file, help='Name of pipeline config .yml file.', required=True)
# args = parser.parse_args()

args = parser.parse_args()

Run(config_file=args.config_file, project_dir=args.project_dir, trigger_class = args.trigger_class)
