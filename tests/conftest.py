# -*- coding: utf-8 -*-
import os
import subprocess
import time

import pytest


@pytest.fixture(scope='session')
def h2o(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_dir)
    proc = subprocess.Popen(
        ['./h2o/h2o-1.5.0/h2o', '-c', './h2o.conf'], shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def fin():
        proc.terminate()
    request.addfinalizer(fin)
    # wait before h2o completely starts
    time.sleep(1)
    return proc
