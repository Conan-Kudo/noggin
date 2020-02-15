from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class OTPForm(FlaskForm):
    description = StringField(
        'Description',
        validators=[
            DataRequired(message='Description must not be empty'),
        ]
    )
