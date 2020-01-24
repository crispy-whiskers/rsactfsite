from flask import Flask
from flask import render_template, request
from what import What
import os, random, selectors, sys
from subprocess import Popen, PIPE
import subprocess


ON_POSIX = 'posix' in sys.builtin_module_names


app = Flask(__name__)


queued = []

@app.route('/')
def home():
     return render_template('index.html')


@app.route('/req')
def process(): 
     print(str(request.values.get('n')))
     cmd = [
          'python3',
          './RsaCtfTool/RsaCtfTool.py',
          '-n',
          str(request.values.get('n')),
          '-e',
          str(request.values.get('e')),
          '--verbose',
          '--private'

     ]
     print('creating process')
     process = Popen(cmd,stdout=PIPE, stderr=subprocess.STDOUT, bufsize=1, close_fds=ON_POSIX)
     s = b''
     while 1:
          if(process.stdout.readline() is b''):
               continue
          b = process.stdout.readline()
          s += b
          if b'END RSA' in s:
               break

     print(s.decode('utf-8'))

     return s





if __name__ == "__main__":
    app.run(debug=True)