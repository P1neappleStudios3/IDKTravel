#
# indexView.py
#
# This class contains the code to be executed when
# the home page URL is requested.
#
################################################################
from flask import render_template
from app import instance

site = 'http://127.0.0.1:5000'

@instance.route('/register')
def register():


    page = 'pages/accounts/register.html'

    title = "Account Registration"

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
                           site=site)