#!/bin/bash/env Python3

# WordPress Mapper Tool

# After running the first mapper 'WordPress_mapper.py' 
# Test your remote target to see which on of the files found are actually installed on the target 

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

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        time.sleep(2)  # Your target may have lockout
        r = requests.get(url)
        if r.status_code == 200:
            answers.put(url)
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')
        sys.stdout.flush()

def run():
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()

    for thread in mythreads:
        thread.join()

if __name__ == '__main__':
    with chdir("/home/user/Downloads/wordpress"):
        gather_paths()
    input('Press return to continue.')

run()
with open('myanswers.txt', 'w') as f:
    f.write(f'{answers.get()}\n')
print('Done')