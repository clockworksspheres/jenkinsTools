# Unit testing Jenkins tools

Tests written to exercise the support libraries - the main tools are
primarily command line interfaces to the libraries in the JenkinsTools
directory.

## Pylint related

Files:

```
PylintIface.py
test_with_pylint.py
test_PylintIface.py
```

harness for running pylint on all the project python files
to expose pylint Error and Failure messages via a python
unittest.

# References:

https://www.jenkins.io/doc/book/pipeline/development/


