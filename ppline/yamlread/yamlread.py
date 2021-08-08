import yaml
from ppline.yamlread.validation.schemes.v1_0 import parse_schema
from ppline.yamlread.validation.schemes.v1_0 import STATIC_DAG_SCHEMA
from ppline.utils import deep_update
from ppline.utils.const import dagmap_consts

class yamlRead(object):
    def __init__(self, dag_path: str, gitlab: False):
        self.gitlab = gitlab
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
        self.stages = [val for val in self.pipeline[dagmap_consts.STEPS_KEYNAME].keys()]

    def _gitlab(self):
        dict_ci = [{}]
        commands=self.commands
        stages=self.stages
        stages.append("test")
            
        dict_ci[0] = {'stages':stages}
        dict_ci.append({'test-app': {'scripts': ['python -V',
                                                'python -c "import sys; print(sys.path)"',
                                                'python -c "import os; print(os.getcwd())"',
                                                'python -c "import ppline"'  
                                                ],
                                    'stage':'test'}})

        for i in range(len(commands)):
            dict_ci.append({stages[i]:{'stage':stages[i],
                                    'script': f'python -m ppline.cli --trigger_class {commands[i]}', 
                                    'retry': {'max': 2}
                                    }
                        })

        with open(r'gitlab_ci.yaml', 'w') as file:
            documents = yaml.dump(dict_ci, file)
        print("gitlab-ci has been successfully created!")
    
    def _yaml(self):
        for i in range(len(self.commands)):
            _file=self.commands[i].split(':')[0][:-3].replace('/', '.')
            _class = self.commands[i].split(':')[1]
            exec(f'from {_file} import {_class}')

            exec(f'c{i} = {_class}()')
            exec(f'c{i}()')

    def executor(self):
        if self.gitlab == True:
            self._gitlab()
        else:
            self._yaml()

    def __call__(self):
        self.parse_pipeline()
        self.extract_executables()
        self.executor()
