# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


''' This file is to develop a flask based python project

'''

from flask import Flask, render_template,request
import tkinter as tk
from tkinter import filedialog as fd

application = Flask(__name__)

posts = [
    {
        'auhtors': 'Copre',
        'title': 'blog',
        'content': 'asdbjna',
        'date_posted': 'Aptilsd fdf',
    },
{
        'auhtors': 'Ankit',
        'title': 'blog 2',
        'content': 'asdbjna 2',
        'date_posted': 'May 27',
    }
]

@application.route('/')
@application.route('/home')
def hello_world():
    return render_template('home.html',posts= posts)


@application.route('/about')
def about():
    return render_template('about.html', title= 'About')


@application.route('/transfer', methods= ["POST", "GET"])
def transfer():
    return render_template('transfer.html')



if __name__== "__main__":
    application.run (debug=True)


