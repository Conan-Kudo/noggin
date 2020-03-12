from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SelectField, TextAreaField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import AnyOf, DataRequired, Email, Optional, Length

from noggin.utility.locales import LOCALES
from noggin.utility.timezones import TIMEZONES


class UserSettingsProfileForm(FlaskForm):
    firstname = StringField(
        'First Name', validators=[DataRequired(message='First name must not be empty')]
    )

    lastname = StringField(
        'Last Name', validators=[DataRequired(message='Last name must not be empty')]
    )

    mail = EmailField(
        'E-mail Address',
        validators=[
            DataRequired(message='Email must not be empty'),
            Email(message='Email must be valid'),
        ],
    )

    locale = SelectField(
        'Locale',
        choices=[(l, l) for l in LOCALES],
        validators=[
            DataRequired(message='Locale must not be empty'),
            AnyOf(LOCALES, message='Locale must be a valid locale short-code'),
        ],
    )

    ircnick = StringField('IRC Nickname', validators=[Optional()])

    timezone = SelectField(
        'Timezone',
        choices=[(t, t) for t in TIMEZONES],
        validators=[
            DataRequired(message='Timezone must not be empty'),
            AnyOf(TIMEZONES, message='Timezone must be a valid timezone'),
        ],
    )

    github = StringField('GitHub Username', validators=[Optional()])

    gitlab = StringField('GitLab Username', validators=[Optional()])

    rhbz_mail = EmailField('Red Hat Bugzilla Email', validators=[Optional()])


class UserSettingsKeysForm(FlaskForm):
    sshpubkeys = FieldList(
        TextAreaField(validators=[Optional()], render_kw={"rows": 4}), label='SSH Keys'
    )

    gpgkeys = FieldList(
        StringField(validators=[Optional(), Length(max=16)]), label='GPG Keys'
    )


class UserSettingsAddOTPForm(FlaskForm):
    description = StringField(
        'Description',
        validators=[DataRequired(message='Description must not be empty')],
    )


class UserSettingsDisableOTPForm(FlaskForm):
    token = HiddenField(
        'token', validators=[DataRequired(message='token must not be empty')]
    )