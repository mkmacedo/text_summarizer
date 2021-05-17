import sys
import subprocess

with open('testreq.txt', 'r') as requirements:
    for line in requirements:
        reqs = subprocess.check_call([sys.executable, '-m', 'pip', 'install', line])

import nltk 
nltk.download('stopwords') 
nltk.download('punkt') 

