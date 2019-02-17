We use Doxygen to automatically create a documentation for our code. 
The documentation can be found [here](https://theslimvreal.github.io/PSE---LA-meets-ML/index.html).

If you are not familiar with the Doxygen syntax for Python, this guide will show you some examples.

### Comments in Python

In Python you have two ways of creating a comment in the code:

```python
"""
This is a mutli-line 
comment.
"""
def test_func():
    pass
```

```python
def test_func():
    #   This is a single line comment
    pass
```

Even though the multi-line commenting style is more popular, Doxygen only supports the comments with a leading `#`.

### Syntax

To properly document a class and its function you need to provide the following things.

#### Classes

```python
##  Some short and basic information that will be displayed in the class overview
#
#   More details description about the class goes here.
#   This can be view by clicking on the class in the generated view.
class ExampleClass:
    pass
```

#### Functions

```python
##  Short description what this function does
#
#   more detailed information about the function.
#   If it's appropriate maybe provide a example usage.
#
#   @param first_input_parameter the first parameter the function receives
#   @param second_parameter the second parameter for the function
#   @return the function returns this
def test_func(first_input_parameter, second_parameter):
    pass
```

It is important that the names after the `@param` exactly match the names defined in the function.
Private functions that have two leading underscores e.g.`def __private_func()`, won't be found in the documentation and therefore don't need to be documented properly.

### Creating Documentation

* Downlaod and install [Doxygen](http://www.doxygen.nl/download.html)
* Open the terminal in the git repository folder
* enter
   >  doxygen Doxyfile
* You can find the progress and errors in the console
* Open the folder `docs/html`
* Search for the `index.html` file and run it with a browser
* Now you can view generate documentation
