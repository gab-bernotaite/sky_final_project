from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class QueryForm(FlaskForm):
    email = StringField('Email address *', validators=[InputRequired()])
    fullname = StringField('Full name *', validators=[InputRequired()])
    telephone = StringField('Your phone number: ')
    project_date = DateField('Project date: ')
    location = SelectField(u'Location: ', choices=[('opt', 'Select'), ('Richmond', 'Richmond'),
                                                   ('Camden', 'Camden'), ('Kensington', 'Kensington'),
                                                   ('Other', 'Other')])
    budget = FloatField('Estimated budget £')
    detail = TextAreaField('Tell me what you are envisioning for your session?')
    services = SelectField(u'What services are you interested in?',
                            choices=[('Select', 'Select'), ('Family Session', 'Family Session'),
                                     ('Portrait Photoshoot ', 'Portrait Photoshoot '),
                                     ('Event Photography ', 'Event Photography '), ('Other', 'Other')])
    recommend = SelectField(u'How did you hear about us? ',
                            choices=[('None', 'Select'), ('Google', 'Google'), ('Social Media', 'Social Media'),
                                     ('Referral', 'Referral'), ('Other', 'Other')])
    submit = SubmitField('Submit')

class Calculator(FlaskForm):
    distance = SelectField(u'Distance',
                           choices=[('Select', 'Select'), ('>10 Miles ', '>10 Miles '),
                                    ('11>50 Miles ', '11>50 Miles '),
                                    ('51>150 Miles ', '51>150 Miles ')])
    duration = SelectField(u'Duration',
                           choices=[('Select', 'Select'), ('30 mins ', '30 mins '),
                                    ('1 hr ', '1 hr '),
                                    ('1.5 hrs ', '1.5 hrs '), ('2 hrs ', '2 hrs '),
                                    ('2.5 hrs ', '2.5 hrs '), ('3 hrs ', '3 hrs '),
                                    ('3.5 hrs ', '3.5 hrs '), ('4 hrs ', '4 hrs '),
                                    ('4.5 hrs ', '4.5 hrs '), ('5 hrs ', '5 hrs '),
                                    ('5.5 hrs ', '5.5 hrs '), ('6 hrs ', '6 hrs '),
                                    ('6.5 hrs ', '6.5 hrs '), ('7 hrs ', '7 hrs '),
                                    ('7.5 hrs ', '7.5 hrs '), ('8 hrs ', '8 hrs '),
                                    ('8.5 hrs ', '8.5 hrs '), ('9 hrs ', '9 hrs '),
                                    ('9.5 hrs ', '9.5 hrs '), ('10 hrs ', '10 hrs ')])

    no_people = StringField('Number of people: ')