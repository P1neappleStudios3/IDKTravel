#
# indexView.py
#
# This class contains the code to be executed when
# the home page URL is requested.
#
################################################################
from flask import render_template, redirect, request
from app.models.accounts.BetaAccount import BetaAccount
from app import instance
from app.settings import *

@instance.route('/landing', methods=['GET', 'POST'])
def landing():
    page = 'pages/landing/landingPage.html'

    if request.method == 'POST':
        email = request.form['email']
        registerResult = BetaAccount.register(email)
        if registerResult == True:
            return "<h1>"+email+"</h1><p>Thank you for registering!  Stay tune for more details!"
        else:
            return "<h1>"+email+"</h1><p>Your email is already entered in our system!"
    else:
        return render_template(page)
