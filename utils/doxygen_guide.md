### Automatic generation of code documentation with Doxygen

Doxygen allows you to automatically create a documentation for you code.
In order to do so, you need to follow the Doxygen-Specific syntax for documenting your code.


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

* Download Doxygen for your operating system
* After installing, search for Doxywizard in you programs and run it
* Step 1: Select the `modules` folder where all the code is located as working directory
* Step 2: 
    -   Also select the `modules` folder as source code directory
    -   Check `Scan recursively`
    -   Select `modules/documentation` as the target directory
* The other fields are optional, you can click next
* Select `Optimize for Java or C# output`
* Click next
* The next two screens can be skipped, just press next
* Press `Run doxygen` and wait for it to finish
* You can find the progress and errors in the console below the run button, please make sure that no errors occur.
* Open the folder `modules/documentation/html`
* Search for the `index.html` file and run it with a browser
* Now you can view generate documentation
