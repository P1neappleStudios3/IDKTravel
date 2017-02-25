

def generate_connection_string(host, database, user, password):
    return "host='"+host+"' dbname='"+database+"' user='"+user+"' password='"+password+"'"

POSTGRES_SERVER = {
    'connection_strings':   {
        'System' : generate_connection_string('localhost', 'System', 'postgres', 'test')
    }
}

SITE = "http://127.0.0.1:5000"

# Turn beta on for landing page
#######################
BETA = False
#######################
