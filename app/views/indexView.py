#
# indexView.py
#
# This class contains the code to be executed when
# the home page URL is requested.
#
################################################################
from flask import render_template, redirect, request, url_for
from app import instance
from app.settings import *



@instance.route('/')
@instance.route('/index')
def index():
    page = 'pages/index/index.html'

    title = "Home"

    if BETA:
        return redirect(url_for('landing'))

    description = "This is a travel planning website"
    keywords = "Travel planning, backpacking, hiking, outdoors"

    openGraph = {
        'og_description'    :   'None',
        'og_title'          :   'None',
        'og_type'           :   'None',
        'og_url'            :   'None',
        'og_image'          :   'None',
        'og_locale'         :   'None',
        'og_site_name'      :   'None'
    }


    return render_template(page,
                           title=title,
                           description=description,
                           keywords=keywords,
                           og_title=openGraph['og_title'],
                           og_type=openGraph['og_type'],
                           og_url=openGraph['og_url'],
                           og_image=openGraph['og_image'],
                           og_description=openGraph['og_description'],
                           og_locale=openGraph['og_locale'],
                           og_site_name=openGraph['og_site_name'],
                           site=SITE)






