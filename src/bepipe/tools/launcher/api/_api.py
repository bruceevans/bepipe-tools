
# TODO Probably need a seperate pipeline module or put in bepipe.core
# TODO JSON stuff from core
from enum import Enum

class SeverityLevel(Enum):
    """Error levels"""

    # TODO move this to core and add colors to the labels
    INFO = "Info" # white
    WARN = "Warning" # yellow
    ERROR = "Error" # red


def create_pipeline(pipeline, launch_list):
    """Create a pipeline with the provided list of applications
    
    Args:
        pipeline (str): Json output file
        launch_list [dict]: List of apps and commands

    Returns:
        bool: Success or fail on file written

    """

def read_pipeline(pipeline):
    """Read a pipeline json file and gather the commands
    
    Args:
        pipeline (str): Path to pipeline json file

    Returns:
        [dict]: List of dictionaries containg the application commands and info

    """

# NOTE (bevans)
# Generic command launcher, intended to launch an exe or run a script
def run_command(cmd):
    """Run a command from an application dictionary
    
    Args:
        cmd (str): Command to run

    Returns:
        bool: Success or fail

    """
