## superset-learning

### Notes
- To start everything
    - `source venv/bin/activate`
    - `superset runserver`
    -  Go to the localhost link.
- https://github.com/airbnb/superset/issues/236 will show you how to specify a connection string that is properly url escaped when adding a database at LOCALLINK/databaseview/add
- To get the quoted connection string run `python connstring.py | pbcopy`
- `venv2` is the python3 venv
- Username for the python2 superset is `josh`


### Setting up

_Python 3_

- `python3 -m venv venv2`
- `. ./venv2/bin/activate`
- Navigate to [here](http://airbnb.io/superset/installation.html) to see superset setup instructions
