import psycopg2
from app.settings import *
from app.utility.email_util import valid_email_format, verify_email_ping


class BetaAccount:

    @staticmethod
    def register(emailaddr):

        # First, start by validating the email argument
        if valid_email_format(emailaddr):
            # Next, verify that the email provided actually exists
            if verify_email_ping(emailaddr):



                # initialize connection object
                connection = None

                # enclose everything in a try block
                try:

                    # Now we can start working with SQL
                    connection = psycopg2.connect(POSTGRES_SERVER['connection_strings']['System'])
                    cursor = connection.cursor()

                    # Next, determine if the email provided already exists in the beta_account
                    selectQuery = """
                    SELECT EMAIL FROM account_storage.beta_account WHERE EMAIL=%(email_input)s
                    """

                    result = cursor.execute( selectQuery, { 'email_input' : emailaddr } )
                    records = cursor.fetchone()

                    if records is not None:
                        # The email already exists in our system; return false
                        cursor.close()
                        connection.close()
                        return False
                    else:
                        # continue with the script and register the
                        # user into the system
                        insertQuery = """
                        INSERT INTO account_storage.beta_account(email) VALUES(%(email_input)s)
                        """
                        cursor.execute(insertQuery, {
                            'email_input': emailaddr
                        })

                        connection.commit()

                    # close cursor object
                    cursor.close()
                except( Exception, psycopg2.DatabaseError) as error:
                    #print("BetaAccountError[~", error, " ]")
                    pass

                finally:
                    # Finally, end by closing connection
                    if connection:
                        connection.close()

                return True

            else:
                # email was not verified
                return False
        else:
            # email was not valid format
            return False


#######################################################

#BetaAccount.register('jacob.perkins94@gmail.com')
#1BetaAccount.register('Jacob.Perkins@rockets.utoledo.edu')


#BetaAccount.register('jacob@gmail.com')
#BetaAccount.register('jacob@utoledo.edu')