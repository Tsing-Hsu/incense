import logging
import yaml

logger = logging.getLogger(__name__)

def load_config_yaml(configfilename = None):
    
    parsed_yaml_file = None

    try:
        a_yaml_file = open(configfilename)
    except FileNotFoundError as error:
        logger.error("File not found: %s", error)
        
    try:
        parsed_yaml_file = yaml.safe_load(a_yaml_file)
    except yaml.YAMLError as exc:
        logger.error("Error in configuration file: %s", exc)
        mark = exc.problem_mark
        logger.error("Error position: (%s:%s)" % (mark.line+1, mark.column+1))     
    
    logger.info("Config file loaded.")

    return parsed_yaml_file