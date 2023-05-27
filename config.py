import os

"""
Setting an environment variable:
1. In the terminal -  export VARIABLE_NAME=value . Validate with echo $VARIABLE_NAME.
2. In python - import OS
3. Use - value = os.environ["VARIABLE_NAME"]
"""

api_key = os.environ["openaiapikey"]
