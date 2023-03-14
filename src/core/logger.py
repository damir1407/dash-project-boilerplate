import os
import logging

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# Make sure to add your custom project name
PROJECT_NAME = ""
LOG_PATH = f"{BASE_PATH}/{PROJECT_NAME}/log/base_loger.log"
logging.basicConfig(level=logging.INFO, filename=LOG_PATH,
                    format="%(asctime)s :: %(levelname)s :: %(message)s")
