from smtplib import *

from configuration import *

debug = True
verbose = True
version = "1.0.0"

key_sender = 'sender'
key_subject = 'subject'
key_username = 'username'
key_password = 'password'
key_receivers = 'receivers'
key_smtp_server = 'smtp_server'
param_configuration_names = '--configuration'


def log(what):
    if verbose:
        print what


def notify(content, configuration_names):
    if configuration_names:
        for configuration_name in configuration_names:
            if debug:
                log("Using '" + configuration_name + "' configuration")
            if configuration_name in configurations:
                configuration = configurations[configuration_name]
                notify_with_configuration(content, configuration)
            else:
                log("There is no configuration with the name: '" + configuration_name + "'")
    else:
        if debug:
            log("Using all configurations.")
        for configuration in configurations:
            notify_with_configuration(content, configuration)


def notify_with_configuration(content, configuration):
    message = """From: %s
    To: %s
    Subject: %s

    %s
    """ % (configuration[key_sender], configuration[key_receivers], configuration[key_subject], content)

    try:
        server = SMTP(configuration[key_smtp_server])
        user = configuration[key_username]
        log("Logging in user: " + user)
        server.login(user, configuration[key_password])
        receivers = configuration[key_receivers]
        log("Sending mail to: " + receivers)
        server.sendmail(configuration[key_sender], receivers, message)
        log("Shutting down connection.")
        server.quit()
        return True
    except (SMTPHeloError, SMTPAuthenticationError, SMTPAuthenticationError, SMTPException,
            SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError) as e:

        print("Error: \n" + str(e))
        pass

    return False
