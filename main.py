import os
from dotenv import load_dotenv
from ratelimiter import RateLimiter
import logging

import db.pgsql_db_utils as dbUtils


# Load environment variables
dotenv_path = os.path.join('../../.env')
load_dotenv(dotenv_path)


class SampleDevice():
    """
    Sample device
    """
    def __init__(self):
        self.conn = dbUtils.create_connection_from_file()
   
        print(f"[INFO]: Initialized Sample Device main module")

        # Set up current logging mechanism
        logging.basicConfig(filename='logs/sample_device.log', filemode='w', format='%(created)f - %(message)s')

    @RateLimiter(max_calls=1, period=1)
    def check_value(self):
        answer = 42

    def run(self):
        """
        Runs the continuous sample device scans

        Returns:
        ------
        `Void`

        """
        while True:
            try:
                self.check_value()
            except Exception as e:
                print(f"[ERROR]: Error running the continuous run loop on sample_module: {e}")
                continue

    
