To install the library:
```bash
pip install ppline
```


# 1. About

The library `ppline` can execute any class or any sequance of classes in any order. In other words, it is able to execute both:
- a specific class from a particular python file that can contain multiple classes, or 
- an ordered sequence of specified classes from different python files.


# 2. How it works

## 2.1. Triggering a sequence of classes in order

To build a pipeline with classes to execute, you have to create a config .yml file in a root directory in the following form:

```text
steps:
    [step name]:
        exec: [relative path to a file]:[class to execute]
    [step name]:
        exec: [relative path to a file]:[class to execute]
    [step name]:
        exec: [relative path to a file]:[class to execute]
```
Let's create a config .yml file with the name `collect.yml`:

```text
steps:
    preProcessing:
        exec: src/calculation.py:Calculate
    kMeans:
        exec: src/models.py:Kmeans
    hyperTuning:
        exec: src/tuning.py:GridSearch
```

The executable classes specified in collect.yml should have a ``__call__`` method. For instance, if we open aforementioned `src/calculation.py` and look at `Calculate` class, we see __call__ method in the end.

```python
#this is src/calculation.py

class Calculate(object):
	def sum(self):
		a=2
		b=4
		self.c=a+b

	def divide(self):
		f=4
		self.d = self.c/f

    def show_result(self):
            print(self.d)

	def __call__(self):
		self.sum()
		self.divide()
        self.show_result()

```

After creating a configuration .yml file in your root directory, use the following command to trigger the pipeline in terminal:

```bash
python -m ppline.cli --config_file collect.yml
```


## 2.2. Triggering one class from .py file
Ppline can also trigger a specific class from a specific .py file. 

```bash
python -m ppline.cli --trigger_class path/to/file.py:TestClass
```

Here is an example of code that triggers a `Calculate` class from `calculation.py` file. Note: TestClass should have a __call__ method that executes desired class functions.

```bash
python -m ppline.cli --trigger_class src/calculation.py:Calculate
```


## 3. To do

- dependency map between steps
- independent steps in parallel
- make png export of visualized pipeline w/ names


# 3. Changes

### 0.2.2 (2021-03-15)

- \_\_call\_\_ method is implemented 
- minor bug fixes
