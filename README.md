# ppline

# 1. About

ppline can trigger your python modules in any specified order, making it look like a pipeline! 


### 1.1. Installation

```bash
pip install ppline
```


### 1.2. How it works

Ppline takes configuration of your pipeline from .yml file, so you have to create it in your root directory in the following form:


```text
steps:
    [step name]:
        exec: [relative path to a file]:[class to execute]
    [step name]:
        exec: [relative path to a file]:[class to execute]
    [step name]:
        exec: [relative path to a file]:[class to execute]
```
Here is the example:

```text
steps:
    preProcessing:
        exec: src/preprocessing.py:Extract
    kMeans:
        exec: src/models.py:Kmeans
    hyperTuning:
        exec: src/tuning.py:GridSearch
```

Any executable class should have a method ``_exec()``, because ppline is searching for that method to execute. Hence:

```python
class SomeFunction(object):
	def sum(self):
		a=2
		b=4
		self.c=a+b

	def divide(self):
		f=4
		self.d = self.c/f

	def _exec(self):
		self.sum()
		self.divide()
    
```

### 1.3. How to use

In your working directory write:

```bash
python -m ppline.cli --pipeline_config file.yml
```


### 1.4. To do

- dependency map between steps
- independent steps in parallel
- make png export of visualized pipeline w/ names

