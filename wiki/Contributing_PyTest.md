For our internal software testing we use PyTest.
The package is useful for unit and integration tests.

## Installation

For using PyTest you need to install it via pip.

> python -m pip install pytest

or just automatically install all our dependencies

> python -m pip -r install requirements.txt

## Create a test

First you create a class the is called something like `test_name.py`.
This is important because PyTest will search for files with a leading `test`.
In that file you create your test function that also needs to have the leading `test_`.

```python
def test_say_hello():
    obj = PyClass()
    result = obj.say_hello()
    assert result == "Hello"
```

## Run tests

To run all the test you can either go to your terminal and enter

> python -m pytest

or you can create a test configuration in PyCharm.

* open `Run`
* click `Edit Configurations`
* hit `+`
* look for `pytest` in `Pyhon tests`
* click `OK`

Now you can select this configuration and press the green run button.