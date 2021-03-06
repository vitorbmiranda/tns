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
    - `job`: schedule/job layer
- `config`: yml files
    - `tns.yml`: db and app configuration
    - `logging.yml`: logging config    
- `logs`: default folder where logs are written (more details
in `config/logging.yml`)


## Setup

### Python Virtual Env

- Install Miniconda
    - https://conda.io/miniconda.html
- Create the virtual env using the environment.yml file in the root of 
the project
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

- Configure it in `config/tns.yml`

- Easier to use a docker container for it though, e.g:

`docker run -d -p 5432:5432 --name tns_postgres -e POSTGRES_PASSWORD=postgres postgres:9.6.12`


## Execution

- Open a terminal with the `tns` virtual env activated
    - It's easier to use PyCharm's terminal option as it starts a terminal
with the configured env activated
- Inside `startup.py` file there' a call to `tsn_startup.main()` with 
some optional env variables thatn be used. Examples:
    - If you want the db to be recreated and some test models to be inserted, 
just use `TNS_RECREATE_TABLES=true TNS_TEST_DB_MODELS=true python startup.py`
    - To change the log level to `INFO` use `TNS_LOG_LEVEL='INFO'`
- Run it
    - `python startup.py`
  
## Extra

- To generate the conda environments.yml file again, with 
the tns source activated:

`conda env export -n tns > environment.yml`


