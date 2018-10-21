# MonkeyPatch

Monkeypatch is a built in pytest fixture that lets you modify the behavior
of existing code. This is sometimes needed with unittests because unittests
are supposed to be "self contained" which means they shouldn't need anything
other than python to run.

In data terms this means no access to
* CSVs
* Databases
* The internet

In these situations were we need to load data, but want to isolate our test suite
monkeypatch is very helpful

## Prior knowledge
Effective use of monkeypatch is based upon knowledge of python module and namespace structure.

Essentially you're performing a precise surgery in Python's functionality, taking out
bits of code here and there to replace functionality. The more you know about how
Python "searches" for code the better off you are.

Keywords to search for. 
* Python module namespace
* Python import machinery
* Python object reference

# Resources
* https://docs.pytest.org/en/latest/monkeypatch.html

