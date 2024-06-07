from flask_cors import CORS
from flask import Flask
import pickle
print(__name__)

app = Flask(__name__)

CORS(app)

with open('dataset.pkl', 'rb') as f:
    words_probability = pickle.load(f)

