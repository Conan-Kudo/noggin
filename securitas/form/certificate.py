from flask_wtf import FlaskForm
from wtforms import FieldList, StringField
from wtforms.validators import DataRequired

class CertificateForm(FlaskForm):
    csr = StringField(
        'CSR', validators=[DataRequired(message='CSR must not be empty'),]
    )
