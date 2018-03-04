import yaml
import logging.config

db_config = None
app_config = None
logger = logging.getLogger(__name__)


def init(filepath):
    """
    Initialize <filepath> file and set up the global dicts <db_config> and
    <app_config>.
     :param filepath: TNS YAML file
    """

    global db_config
    global app_config

    with open(filepath, "r") as stream:
        yaml_config = yaml.safe_load(stream)
        logger.debug("YAML file read: {}".format(yaml_config))
        db_config = yaml_config['db']
        app_config = yaml_config['app']