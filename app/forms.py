from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileAllowed

class createPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Descrpiption', validators=[InputRequired()])
    room_num = StringField('No. of Rooms', validators=[InputRequired()])
    bathroom_num = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()]) 
    property_type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Image File', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    