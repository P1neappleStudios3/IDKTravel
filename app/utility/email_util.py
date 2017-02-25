# Name:
#
#
#
#
#
#
##################################################################
import re
from dns import resolver
import socket
import smtplib

# The purpose of this function is to determine whether the string
# passed as an argument is of a valid email format.
def valid_email_format(emailaddr):

    EMAIL_REGEX = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    match = re.match(EMAIL_REGEX, emailaddr)
    if match is None:
        return False
    else:
        return True



# The purpose of this code is to ping the email address to determine
# if the email address actually exists.
#
# Return true if email is verified
# Return false if email is NOT verified
#
def verify_email_ping(emailaddr):

    # Pull the domain name from the email address
    domain_name = emailaddr.split('@')[1]

    # Get the MX record for the domain
    records = resolver.query(domain_name, 'MX')

    mx_record = records[0].exchange
    mx_record = str(mx_record)

    # ping email server
    # (check if the email address exists)

    # get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP conversation
    server.connect(mx_record)
    server.helo(host)
    server.mail(emailaddr)

    code, message = server.rcpt(str(emailaddr))
    server.quit()

    if code == 250:
        return True
    else:
        return False


#######################################################