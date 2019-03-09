import logging.config
import yaml
import os

import tns.cfg.config as tns_config
import tns.db.database as tns_database
import tns.db.test_models as test_models
import tns.job.scheduler as tns_scheduler
import tns.crypto.tns_crypto as tns_crypto

logger = None


def __load_log_config(
    file_path
):
    """
    Load log configs in a yml file

    :param file_path:  yml file with logging definitions
    :return:
    """
    try:
        with open(file_path, 'rt') as f:
            log_config = yaml.safe_load(f.read())
        logging.config.dictConfig(log_config)
        print("Initialized logging config from file {}".format(file_path))
    except Exception:
        default_level = logging.INFO
        print("** An error occurred while loading the logging file {}. "
              "Using default logging config.".format(file_path))
        logging.basicConfig(level=default_level)


def __load_tns_config(config_file):
    """
    Load TNS main config file

    :param config_file: YAML file
    """
    tns_config.init(config_file)
    logger.info("Initialized cfg file: {}".format(config_file))


def __build_db_url(db_config):
    """
    Builds the DB connection URL

    :param db_config: dict with the db parameters
    """

    # builds the URL that will be passed later to SQL Alchemy
    # using the info in the TNS config file
    url = db_config['conn_url'].format(
        user=db_config['user'],
        pwd=db_config['pwd'],
        host=db_config['host'],
        database=db_config['database'])

    return url


def main(
    start_scheduler: True,
    **kwargs
):
    """
    :param start_scheduler: should start the scheduler or not
    :param kwargs:
        tns_config_file: tns config file path
            Default: <root>/config/tns.yml
        tns_logging_config_file: tns logging config file path
            Default: <root>/config/logging.yml
        logging_level: log level that overwrites the level in the file
            Default: whatever is defined in the logging file or INFO if
            any error happens
        create_database_objects: if True it recreates the db schema
            Default: False
        test_db_models: if True it does some testing with Models
            Default: False
    """
    global logger

    tns_config_file = kwargs.get('tns_config_file', 'config/tns.yml')
    tns_logging_config_file = kwargs.get('tns_logging_config_file', 'config/logging.yml')
    create_database_objects = kwargs.get('create_database_objects', False)
    test_db_models = kwargs.get('test_db_models', False)

    # initialize log config
    __load_log_config(file_path=tns_logging_config_file)

    # if a log level parameter was passed, set it in the logger instance
    log_level = os.environ.get('TNS_LOG_LEVEL')
    if log_level:
        logging.getLogger().setLevel(log_level)

    # instanciate the logger
    logger = logging.getLogger(__name__)

    # initialize cfg
    __load_tns_config(tns_config_file)

    # initialize DB
    db_url = __build_db_url(tns_config.db_config)
    logger.debug("Final DB URL: {}".format(db_url))
    tns_database.init(db_url)

    logger.info("Initialized DB structure using the URL: {}".format(db_url))

    # initialize crypto module
    key_location = tns_config.app_config['crypto_key']
    tns_crypto.init(key_location)

    # recreate db
    if os.environ.get('TNS_RECREATE_TABLES') == 'true':
        logger.warning("Recreating TNS tables")
        tns_database.create()
        logger.warning("TNS tables dropped and created again!")

    if os.environ.get('TNS_TEST_DB_MODELS') == 'true':
        logger.warning("Inserting dummy models instances")
        test_models.do_test()
        logger.warning("Done inserting dummy models!")

    if start_scheduler:
        tns_scheduler.run()
        logger.info("TNS initialized!")

