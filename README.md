# Clean Imports in Python

## Setting Up 

Read this for a reference on packaging:  (important even if annoying)
  https://python-packaging.readthedocs.io/en/latest/minimal.html

don't worry about the "publishing on pypi" part, that's not important if you're not going to publish. 

your directory structure should look like this:
```
└── my_project (ROOT)
    ├── my_project
    │ ├── package1
    │ │   ├── __init__.py
    │ │   ├── module1.py
    │ │   └── module2.py
    │ │
    │ ├── package2
    │ │   ├── __init__.py
    │ │   ├── module3.py
    │ │   └── subpackage1
    │ │       └── module4.py
    │ ├── tests
    │ │   ├── __init__.py
    │ │   └── test_module1.py
    │ ├── main.py
    │ └── __init__.py
    └── setup.py

```

### Importing

Make sure that any code in a package is not dependent on code in another package(e.g., package1.module1.py doesn't import anything from package2.module3). This makes your code much cleaner and your dependencies less tangled up, and prevents you from having to do the awful `sys.path.insert()` bs. 

```python
# my_project/main.py

from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2
```

```python
# my_project/package1/module1.py

from .module2 import function1  #  import function1 from module2 in current package (package1) 
```

```python
# my_project/package2/module3.py

from . import class1    #  import class1 from current package (package2)
from .subpackage1.module5 import function2  #  import function2 from subpackage1 in current package (package2)
```


open `setup.py` and copy the following into it and add your information:
```python
from setuptools import setup

setup(name='<project-name>',
      version='0.0.1',
      description='',
      url='', # github repo   
      author='<your-name or github-id>',
      author_email='<your-email>',
      license='MIT',
      packages=['<project-name>'],
      zip_safe=False)
```

Then you can run `pip install -e .` from the root of your project. This installs your package to the system with a symlink so that your changes to the source are widely available. 

Nonetheless, I still recommend that you run it again after major changes so that you get a clean install. 

You can also simply run `pip install .` but that doesn't create a symlink. 

## Testing

I also super recommend having a test suite that allows you to run all your code and test that it works; this is also where I normally print things out for demos. 

Open `my_project/package1/module1.py` and copy the following into it:


```python
# -*- coding: utf-8 -*-
import argparse
import sys
import logging

__author__ = "<author>"
__copyright__ = "<author>"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
```

Create a test file in `my_project/tests/test_module1.py` and copy the following inside of it:

```python
# -*- coding: utf-8 -*-

from my_project.package1.module1 import fib

from unittest import TestCase

__author__ = "<author>"
__copyright__ = "<author>"
__license__ = "mit"


class TestFib(TestCase):
    def test_fib(self):
        print("Running tests in test_fib:") 
        print(f"\tfib(1) == {fib(1)}")
        self.assertTrue(fib(1) == 1)
        
        print(f"\tfib(2) == {fib(2)}")
        self.assertTrue(fib(2) == 1)
        
        print(f"\tfib(1) == {fib(7)}")
        self.assertTrue(fib(7) == 13)

```


From the root of your project, run `python -m unittest my_project/tests/test_module1.py` 

Add your own test suite and you're all set! 
