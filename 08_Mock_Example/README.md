# Mock
Mock lets you create fake objects in Python. For example
instead of actually creating a dataframe we can fake some of the functionality
in a dataframe.  

This is useful because sometimes its expensive or impossible to create the real thing
over and over again. Two examples

* Fitting a model. This could take hours, why not just fake a finished model for your tests?

* Calling an api. Twitter and Google allowed limited usage of free apis. If you keep testing
against their real apis you'll run out of tries. Mock lets you fake http requests so you
don't have to practice against the real thing

* A database response, especially when you don't have access to the database
