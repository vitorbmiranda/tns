# The-elite Notification System (TNS)

## Overview

- **add more stuff here**

### Project structure

- `startup.py`: starts everything (**we still need to adapt some things when
the job framework is added**)
- `tns`
    - `cfg`: config layer
    - `db`: database layer
        - `model`: one file for every table in DB
- `config`: yml files
    - `tns.yml`: db and app configuration
    - `logging.yml`: logging config    
- `logs`: default folder where logs are written (more details
in `config/logging.yml`)


## Setup

### Python Virtual Env

- Install Miniconda
    - https://conda.io/miniconda.html
- Create the virtual env using the environment.yml file in the root of the project
    - `conda env create -f environment.yml -n tns`
- In PyCharm Preferences > Project > select the project and set the 'tns' 
    env you just created

### Database

- Install latest PostgreSQL (e.g 9.6.5)
- Create a user and a database, ex:

```
# create the user, fill in the info
createuser -P --interactive

# create user with the owner as whatever user you created above
createdb -O <user>

# test it out
psql -h localhost <user> -U <pass>
```

- Configure it in config/tns.yml

## Execution

- Open a terminal with the `tns` virtual env activated
    - It's easier to use PyCharm's terminal option as it starts a terminal
    with the configured env activated
- Inside `startup.py` file there' a call to `tsn_startup.main()` with some optional parameters.
Examples:
    - If you want the db to be recreated and some test models to be inserted, just use
        - `create_database_objects=True` and `test_db_models=True`
    - To change the log level to `INFO` use `logging_level='INFO'`
        
- Run it
    - `python startup.py`
  