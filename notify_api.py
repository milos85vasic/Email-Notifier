from smtplib import *

from configuration import *

key_sender = 'sender'
key_subject = 'subject'
key_username = 'username'
key_password = 'password'
key_receivers = 'receivers'
key_smtp_server = 'smtp_server'


def notify(content, configuration_names):
    if configuration_names:
        for configuration_name in configuration_names:
            configuration = configurations[configuration_name]
            notify(content, configuration)
    else:
        for configuration in configurations:
            notify(content, configuration)


def notify(content, configuration):
    message = """From: %s
    To: %s
    Subject: %s

    %s
    """ % (configuration[key_sender], configuration[key_receivers], configuration[key_subject], content)

    try:
        server = SMTP(configuration[key_smtp_server])
        server.login(configuration[key_username], configuration[key_password])
        server.sendmail(configuration[key_sender], configuration[key_receivers], message)
        server.quit()
        return True
    except (SMTPHeloError, SMTPAuthenticationError, SMTPAuthenticationError, SMTPException,
            SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError) as e:

        print("Error: \n" + str(e))
        pass

    return False
