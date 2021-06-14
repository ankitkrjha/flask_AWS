# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


''' This file is to develop a flask based python project

'''

from flask import Flask, render_template,request, url_for


application = Flask(__name__)

posts = [
    {
        'auhtors': '',
        'title': 'Features',
        'content': '',
        'date_posted': '',
    },
{
        'auhtors': '',
        'title': 'Application',
        'content': '',
        'date_posted': '',
    }
]

@application.route('/')
@application.route('/home')
def hello_world():
    return render_template('home.html',posts = posts)


@application.route('/about')
def about():
    return render_template('about.html', title = 'About')


@application.route('/transfer', methods = ["POST", "GET"])
def transfer():
    return render_template('transfer.html')

# adadbabdba
# Hello There

if __name__== "__main__":
    application.run (debug=True)


