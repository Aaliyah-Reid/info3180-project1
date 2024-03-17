from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileAllowed
from flask_wtf.csrf import CSRFProtect

class createPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    num_rooms = StringField('No. of Rooms', validators=[InputRequired()])
    num_bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()]) 
    property_type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Image File', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    