from __future__ import print_function
import pickle
import random
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Class for Events
class Event:
    id: str
    name: str
    description: str
    date: str
    organizers: str

    def __init__(self, id, name, description, date, organizers):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.organizers = organizers

# Class for Tutors
class Tutor:
    id: str
    name: str
    grade: str
    personality: str
    image: str
    school: str
    bio: str
    email: str
    subject: str
    gender: str
    math: str
    science: str
    english: str
    languages: str
    standardized: str
    history: str

    # Constructor for Tutor
    def __init__(self, id, name, grade, personality, image, school, bio, email, gender, math, science, english, languages, standardized, history):
        self.id = id
        self.name = name
        self.grade = grade
        self.personality = personality
        self.image = image
        self.school = school
        self.bio = bio
        self.email = email
        self.gender = gender
        self.math = math
        self.english = english
        self.languages = languages
        self.standardized = standardized
        self.history = history
        self.science = science

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Ug1WzgoT1R32E8Y1yYdanYfab3Yz2JIWrMLBzC0WmV4'
SAMPLE_RANGE_NAME = 'Updated Students!A2:N'
EVENTS_RANGE_NAME = 'Events!A2:E'

def get_data():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('classes/token.pickle'):
        with open('classes/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'classes/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('classes/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # Calling the Tutors Data
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    # Calling the Events Data
    event_result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=EVENTS_RANGE_NAME).execute()
    event_values = event_result.get('values')

    # Blank Array of Tutors
    tutors = []

    # Blank Array of Events
    events = []

    # Creating Array of Tutors
    if not values:
        print('No tutor data found.')
    else:
        i = 1
        for row in values:

            """ Creating Random Image """
            image_number = random.randint(1, 7)
            image_name = ""

            if (row[4] == "M"):
                image_name = "man_" + str(image_number) + ".png"
            else:
                image_name = "woman_" + str(image_number) + ".png"

            new_tutor = Tutor(id = i, name=row[0], grade=row[1], personality=row[6], image=image_name, school=row[2], bio=row[7], email=row[3], gender=row[4], math=row[8], science=row[9], english=row[10], languages=row[11], standardized=row[12], history=row[13])
            tutors.append(new_tutor)
            i = i + 1
    
    # Creating Array of Events
    if not event_values:
        print('No event data found.')
    else:
        i = 1
        for row in event_values:
            print(row[1])
            new_event = Event(id = i, name=row[0], date=row[1], description=row[2], organizers=row[3])
            events.append(new_event)
            i = i + 1
    
    # Returning Tutors
    return tutors, events