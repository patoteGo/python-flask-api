import flask
import json
import json
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
     # suppose you have some information in a json variable
    # some_data = { "name": "Bobby", "lastname": "Rixer" }
    # you can convert that variable into a json string like this
    json_text = flask.jsonify(todos)
    return json_text
    # return 'hello'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    
    request_body = request.data
    todos.append(json.loads(request.data))
    print("Incoming request with the following body", request_body)
    return flask.jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position-1)
    return flask.jsonify(todos)
    # return 'something'

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)