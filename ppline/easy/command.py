from typing import Optional
import os
from ppline.yamlread.yamlread import Yamlread

class Run:
    def __init__(self, pipeline_config=str, project_dir: Optional[str] = None):
        
        self.pipeline_config = pipeline_config
        self.project_dir = project_dir
        
        if self.project_dir is not None:
            path = self.project_dir+'/'+self.pipeline_config
            if os.path.exists(path)==False:
                raise Exception(f'Cannot find a config file at path {path}')
            PROJECT_DIR_KEYNAME=path
            return PROJECT_DIR_KEYNAME
        else:
            PROJECT_DIR_KEYNAME = self.pipeline_config
            
        execute=Yamlread(dag_path=PROJECT_DIR_KEYNAME)
        execute()