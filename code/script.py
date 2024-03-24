import json
import ast
from flask import Flask, request
from types import SimpleNamespace
app = Flask(__name__)

# route relevant to the hello world
@app.route('/hw/healthCheck', methods=['GET'])
def health_check():
    return "Hello, World!!!"

if __name__ == "__main__":
    app.run()