**For a productive workflow in our team it is important to follow this guidelines.**
**If you want to contribute, please follow this rules.**

## Classes
* classnames in **UpperCamelCase** e.g. `class CommandLineInterface:`
* class inheritances are written in brackets after the classname e.g `class ClassName(SuperClass):`

## Interfaces
* interfaces are simulated by classes with empty methods, raising an exception e.g.:
```Python
class OutputService:
    def print_line(self, line: str) -> None:
        raise Exception("NotImplementedException")
		
    def print_stream(self, message: str, observable: Observable) -> None:
        raise Exception("NotImplementedException")
		
    def print_matrix(self, matrix: Matrix) -> None:
        raise Exception("NotImplementedException")
		
```
* To implement interfaces, just extend them. e.g `class CLIOutputService(OutputService):`

## Attributes
* attribute names are lower case and words are separated by underscores. e.g.: `new_message`
* the desired is written after the attribute name separated by a **:** e.g. `message: str`
* an attribute is set private by leading double underscores e.g. `__message: str`
* an attribute is set static by just declaring it in the class body e.g. for a private static attribute:
```Python
class OutputService:
    __message: str
```
* an object attribute is declared by just setting it in the constructor e.g:
```Python
class OutputService:
    __init__(self, message: str):
        self.__message = message
```
* getters can be realized with the @property tag. e.g.:
```Python
@property
def message(self) -> str:
    return self.__message
```

* setters can be realized with the @attribute.setter tag. e.g.:
```Python
@message.setter
def message(self, message: str):
    self.__message = message
```

## Methods
* method names are lower case and words are separated by underscores. e.g.: `some_method()`
* methods are set static by the @staticmethod tag. e.g.:
```Python
@staticmethod
def util_method():
    pass
```
* non-static methods **always** have the self parameter as their first parameter:
```Python
def non_static_method(self):
    pass
```
* methods are set private by leading double underscores:
```Python
def __private_non_static_method(self):
    pass
```
* same as attributes, parameters can also have a desired type: `method(self, message: str)`
* the method return type can be specified by adding an arrow. e.g:
```Python
@property
def message(self) -> str:
    return self.__message
```
