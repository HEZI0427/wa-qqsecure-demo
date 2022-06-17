# -*- coding: UTF-8 -*-
import os
from uitrace.api import *

log_path = os.path.abspath(os.path.join(__file__, "..", "log"))
if os.path.exists(log_path):
    log_dirs = os.listdir(log_path)
    for dir in log_dirs:
        dir_path = os.path.join(log_path, dir)
        generate_report(dir_path)
        cloud_test_report(dir_path, only_log=True)
