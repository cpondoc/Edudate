from flask import Flask, render_template, send_from_directory, request
from classes.fetch_data import get_data
from classes.send_mail import send_mailtutor
app = Flask(__name__)

ASSET_FOLDER = 'assets/'
STYLE_FOLDER = 'style/'
app.config['ASSET_FOLDER'] = ASSET_FOLDER
app.config['STYLE_FOLDER'] = STYLE_FOLDER

tutors, events = get_data()

@app.route('/category/<subject>')
def view_category(subject):
    tutors, events = get_data()
    
    correct_tutors = []

    for tutor in tutors:
        if (subject == "languages"):
            if tutor.languages != "N/A":
                correct_tutors.append(tutor)
        if (subject == "science"):
            if tutor.science != "N/A":
                correct_tutors.append(tutor)
        if (subject == "math"):
            if tutor.math != "N/A":
                correct_tutors.append(tutor)
        if (subject == "history"):
            if tutor.history != "N/A":
                correct_tutors.append(tutor)
        if (subject == "english"):
            if tutor.english != "N/A":
                correct_tutors.append(tutor)
        if (subject == "standardized"):
            if tutor.standardized != "N/A":
                correct_tutors.append(tutor)
    
    return render_template('category.html', subject = subject.capitalize(), tutors=correct_tutors)

@app.route('/tutors/<string:id>/')
def tutor(id):
    index = int(id) - 1
    return render_template('tutor.html', id = id, tutor = tutors[index])

@app.route('/tutors/<string:id>/reach-out', methods=['GET', 'POST'])
def reach_out(id):
    
    # Getting the data
    if request.method == 'POST':
        result = request.form
    
    # Saving the data
    request_email = result['email']
    request_name = result['student-name']
    description = result['student-description']

    # Getting tutor info
    index = int(id) - 1
    tutor_name = tutors[index].name
    tutor_email = tutors[index].email

    # Making the request
    send_mailtutor(request_name, request_email, tutor_name, tutor_email, description)

    return render_template('confirmation_submission.html', tutor=tutors[index])

@app.route('/assets/<filename>')
def asset_file(filename):
    return send_from_directory(app.config['ASSET_FOLDER'], filename)

@app.route('/style/<filename>')
def style_file(filename):
    return send_from_directory(app.config['STYLE_FOLDER'], filename)

@app.route('/')
def return_home():
    return render_template('index.html')

@app.route('/tutors')
def return_tutors():
    tutors, events = get_data()
    return render_template('tutors.html', tutors=tutors)

@app.route('/events')
def return_events():
    tutors, events = get_data()
    return render_template('events.html', events=events)

@app.route('/about')
def return_about():
    return render_template('about.html')

@app.route('/contact')
def return_contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
