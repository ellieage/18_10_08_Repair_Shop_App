from flask import *
# from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def application():
    return render_template(
        'index.html',name='joe')

@app.route('/<string:subtopic>', methods=['POST'])
def my_form_post():

    l = request.form['length']
    w = request.form['width']
    h = request.form['height']

    return render_template('index.html',**locals())

if __name__ == "__main__":
    app.run()
