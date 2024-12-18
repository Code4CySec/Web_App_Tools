#!/bin/bash/env Python3

# WordPress Mapper Tool

# This is a purpose-built scanner that can hunt for files that are reachable on the remote target.
# It can help you root out leftover files directories protected by '.htaccess' and more.

import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERED = [".jpg", ".gif", ".png", ".css"]
TARGET = "http://Target Here/wordpress"
THREADS = 10

answers = queue.Queue()
web_paths = queue.Queue()

def gather_paths():
    for root,_, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)

@contextlib.contextmanager
def chdir(path):
    """
    On enter, change directory to specified path.
    On exit, change directory back to original.
    """

    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)

if __name__ == '__main__':
    with chdir("/home/user/Downloads/wordpress"):
        gather_paths()
    input('Press return to continue.')