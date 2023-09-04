from flask import Flask

app = Flask(__name__)

# Import the routes module
from app import routes
