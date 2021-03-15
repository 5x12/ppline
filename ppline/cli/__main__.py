import argparse
import os
import pathlib
from typing import Optional
from ppline.easy.command import Run



def _arg_directory(arg):
    expanded = os.path.expanduser(arg)
    if os.path.isdir(expanded):
        return os.path.abspath(os.path.normpath(expanded))
    else:
        raise Exception(f'Argument {arg} must be an existing directory.')


def _arg_pipeline_config(arg):
    # if arg is None:
    #     print('no arg for pipeline')
        # raise TypeError(f'Must specify .yml pipeline config file.')
    if pathlib.Path(arg).suffix not in ['.yml', '.yaml']:
        raise Exception(f'Argument {arg} must be a .yml/.yaml file.')
    if os.path.exists(arg)==False:
        raise Exception(f'Cannot find {arg} at your directory')
    return arg


parser = argparse.ArgumentParser()
parser.add_argument('--project', '-p', type=_arg_directory, default=None, help='Path to project.')

req_grp = parser.add_argument_group(title='Required')
req_grp.add_argument('--pipeline_config', type=_arg_pipeline_config, help='Pipeline config .yml file.', required=True)

args = parser.parse_args()

Run(pipeline_config=args.pipeline_config, project_dir=args.project)
