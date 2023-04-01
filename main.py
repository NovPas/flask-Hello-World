from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/test')
def test():
  return 'test!'
  
app.run(host='0.0.0.0', port=8080)
