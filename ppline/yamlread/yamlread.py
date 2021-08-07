import yaml
from ppline.yamlread.validation.schemes.v1_0 import parse_schema
from ppline.yamlread.validation.schemes.v1_0 import STATIC_DAG_SCHEMA
from ppline.utils import deep_update
from ppline.utils.const import dagmap_consts



class yamlRead(object):
    def __init__(self, dag_path: str):
        self.pipeline = {}
        with open(dag_path, 'r') as inf:
            stream = '\n'.join(inf.readlines())
        try:
            deep_update(self.pipeline, yaml.load(stream, yaml.Loader))
        except yaml.YAMLError:
            raise Exception("Invalid YAML.")
    
    def parse_pipeline(self) -> dict:
        """Parse a raw user pipeline. Currently just validate the schema.

        :param dict pipeline: A raw pipeline passed to Dagestator.
        :return dict: The parsed pipeline.
        """
        self.pipeline= parse_schema(self.pipeline, STATIC_DAG_SCHEMA)

    def extract_executables(self):
        
        self.commands = [val[dagmap_consts.EXEC_KEYNAME] for val in self.pipeline[dagmap_consts.STEPS_KEYNAME].values()]

    def executor(self):
        for i in range(len(self.commands)):
            _file=self.commands[i].split(':')[0][:-3].replace('/', '.')
            _class = self.commands[i].split(':')[1]
            exec(f'from {_file} import {_class}')
            
            exec(f'c{i} = {_class}()')
            exec(f'c{i}()')

    def __call__(self):
        self.parse_pipeline()
        self.extract_executables()
        self.executor()



        



