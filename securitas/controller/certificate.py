from flask import render_template, session

from securitas import app
from securitas.form.certificate import CertificateForm
from securitas.utility import with_ipa

@app.route('/certificate/generate/', methods=['GET', 'POST'])
@with_ipa(app, session)
def certificate_generate(ipa):
    csr_form = CertificateForm()
    if csr_form.validate_on_submit():
        # Call into IPA and ask it for a certificate.
        pass
    return render_template('certificate.html')
