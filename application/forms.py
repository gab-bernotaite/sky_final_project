from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, TextAreaField, SelectField, IntegerField
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
    distance = IntegerField('This is the distance')
    duration = IntegerField('by the hour')
    no_people = IntegerField('Number of people: ')
    calc = SubmitField('Get Quote')