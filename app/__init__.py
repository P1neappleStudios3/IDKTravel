from flask import Flask
from app.settings import *

# create instance of Flask
instance = Flask(__name__, template_folder='templates/')



# import the views below
if BETA:
    import app.views.landing
else:
    import app.views.indexView
    # import app.views.accounts.registerView
    # import app.views.accounts.loginView
    # import app.views.accounts.accountRecoveryView

#import app.views.accounts.accountView