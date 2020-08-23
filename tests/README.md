# Tests folders

Type "`python -m unittest`" in the project's root folder will trigger unit tests that is inside this folder.

Any file prefixed with "`test`" will be automatically tested, as expected in the normal norm of Python unittest. But some files here worth to write about, as it have non standard role:

* `get_long_strings.py`: Executes this file by command line, then prints the mock data. Usefull if it is needed to create a new test that will deal with mocked data.
* `LongStringsSG`: The object that return mocked data. The "`SG`" stands for "Security Group", that is an AWS entity that the object mocks as the bigger string.
