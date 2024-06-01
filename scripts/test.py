from dotenv import load_dotenv

load_dotenv()

import os

print(os.getenv('ALLEN_CACHE'))

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
