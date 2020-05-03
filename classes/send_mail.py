# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mailtutor(requester, requester_email, tutor, tutor_email, description):

    # Creating Request for New Tutoring Service
    message = Mail(
    from_email='app.edudate@gmail.com',
    to_emails= str(tutor_email),
    subject='New Tutoring Request from ' + str(requester),
    html_content='<h4>Hello there, ' + str(tutor) + '!<//h4><br><p>' + str(requester) + ' recently requested you for help on a tutoring session.<br//><br//>Here was the message:<br//><br//>' + str(description) + '<br//><br//>You can reach out to him at:<br//><br//>' + str(requester_email) + '<//p>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

    # Creating Confirmation for New Tutoring Service
    message = Mail(
    from_email='app.edudate@gmail.com',
    to_emails= str(requester_email),
    subject='Confirmation for Tutoring Request from ' + str(tutor),
    html_content='<h4>Hello there, ' + str(requester) + '!<//h4><br><p>You recently requested ' + str(tutor) + ' for help on a tutoring session.<br//><br//>Here was the message you left them:<br//><br//>' + str(description) + '<br//><br//>They will reach out to you at:<br//><br//>' + str(requester_email) + '<//p>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

    # Creating Update Email
    message = Mail(
    from_email='app.edudate@gmail.com',
    to_emails= 'chris.pondoc@gmail.com',
    subject='New Tutoring Submission on Edudate!',
    html_content='Looks like ' + str(requester) + 'just signed up for a tutoring request from ' + str(tutor) + '!')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
