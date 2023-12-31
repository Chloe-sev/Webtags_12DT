from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webpages')
def render_webpage():
  return
  render_template('webpages.html')

@app.route('/styles')
def render_styles():
  return
  render_styles('styles.html')

app.run(host='0.0.0.0', port=81)
