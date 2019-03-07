"""
Infrastructure around downloadable problem sets.
"""

import os
import sys
import tempfile 
import shutil 

import urllib.request 

from course import loader 

from IPython.display import HTML, Markdown, display
import sqlite3
import pandas as pd

def load(url):
    global mod 
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as tmp_file:
            shutil.copyfileobj(response, tmp_file) 
            tmp_file.flush()
            mod = loader.load(tmp_file.name)

def get_question(name=None):
    global mod
    return mod['module'].get_question(mod['module'], name)
    
