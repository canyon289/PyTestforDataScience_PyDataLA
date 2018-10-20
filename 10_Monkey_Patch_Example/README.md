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


# Resources
* Insert pytest monkeypatch documentation

