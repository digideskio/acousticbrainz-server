"""
This script calculates accuracy of models produced by datasets submitted for challenges.
"""
from __future__ import print_function

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import config

from dataset_eval import gaia_wrapper
from dataset_eval import artistfilter
import db
import db.data
import db.dataset
import db.dataset_eval
import db.exceptions
import utils.path
import tempfile
import logging
import shutil
import time
import json
import os


SLEEP_DURATION = 30  # number of seconds to wait between runs


def main():
    logging.info("Starting challenge submissions evaluator...")
    while True:
        db.init_db_engine(config.SQLALCHEMY_DATABASE_URI)
        pending_job = db.dataset_eval.get_next_pending_job()
        if pending_job:
            logging.info("Processing job %s..." % pending_job["id"])
            evaluate_dataset(pending_job)
        else:
            logging.info("No pending models. Sleeping %s seconds." % SLEEP_DURATION)
            time.sleep(SLEEP_DURATION)


def measure_accuracy(model, validation_map):
    raise NotImplementedError


if __name__ == "__main__":
    main()
