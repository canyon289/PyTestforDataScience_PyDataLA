# Concepts introduced

* Test and module directory structure
* Fixtures
* Helpful pytest flags

## Test and Module directory structure
* Add references here to putting tests in module directory or out of module directory

## Fixtures
Fixture syntax for pytest is 
```
@pytest.fixture(scope="fixture_scope")
def my_fixture():
    return fixture_object
```
Fixtures reuse mutable objects, in other words fixtures save your computer
time from setting things up over and over again. They save you time from
typing the same code in over and over again

* https://docs.pytest.org/en/latest/fixture.html#pytest-fixtures-explicit-modular-scalable
* https://docs.pytest.org/en/latest/fixture.html#scope-sharing-a-fixture-instance-across-tests-in-a-class-module-or-session

## Helpful pytest flags

`pytest -v my_library/tests` is verbose mode and prints more information about
tests and prints more information about test runs
