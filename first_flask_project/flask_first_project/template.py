from flask import Flask, render_template

app=Flask(__name__)

@app.route('/templates')
def template():
    return render_template('index.html')

