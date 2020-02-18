from flask import flash, redirect, render_template, session, url_for
import python_freeipa
import uuid

from securitas import app
from securitas.form.otp import OTPForm
from securitas.representation.otptoken import OTPToken
from securitas.utility import with_ipa

@app.route('/otp/')
@with_ipa(app, session)
def otp_listing(ipa):
    username = session.get('securitas_username')
    resp = [
        OTPToken(t) for t in ipa._request(
            'otptoken_find',
            [],
            {'ipatokenowner': username})['result']
    ]
    otp_uri = session.get('otp_uri')
    # Reset this so we only show it once.
    session['otp_uri'] = None
    return render_template('otp/list.html', tokens=resp, otp_uri=otp_uri)

@app.route('/otp/delete/<tokenid>/')
@with_ipa(app, session)
def otp_delete(ipa, tokenid):
    try:
        ipa._request(
            'otptoken_del',
            [],
            {'ipatokenuniqueid': tokenid})
        flash('Deleted the token.', 'success')
    except:
        # TODO: Error handling
        flash('Could not delete the token.', 'danger')
    return redirect(url_for('otp_listing'))

@app.route('/otp/add/', methods=['GET', 'POST'])
@with_ipa(app, session)
def otp_add(ipa):
    form = OTPForm()
    if form.validate_on_submit():
        username = session.get('securitas_username')
        token_id = uuid.uuid4()
        description = form.description.data
        try:
            resp = ipa._request(
                'otptoken_add',
                [],
                { 'ipatokenowner': username,
                  'ipatokenotpalgorithm': 'sha512',
                  'description': description,
                })
            session['otp_uri'] = resp['result']['uri']
        except Exception as e:
            # TODO: Error handling
            flash('Could not add the token.', 'danger')
            flash(e)
        return redirect(url_for('otp_listing'))
    return render_template('otp/add.html', form=form)
