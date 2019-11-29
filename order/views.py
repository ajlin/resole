from flask import render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import PasswordField, StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

from order import app

# photo configuration
photos = UploadSet('photos', IMAGES)
configure_uploads(app,photos)
patch_request_class(app, 5 * 1024 * 1024) #set max upload size to 5mb


class OrderForm(FlaskForm):
    first = StringField('First Name',
                        validators=[DataRequired()]
                        )
    last = StringField('Last Name',
                         validators=[DataRequired()]
                         )
    email = StringField('Email Address',
                        validators = [DataRequired(), Email("please enter a valid email address")]
                        )
    quote = BooleanField('Quote Requested')
    upload = FileField('Photo Upload',
                      validators = [FileAllowed(photos, "Images only!")])
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        filename = photos.save(form.upload.data)
        file_url = photos.url(filename)
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)
    '''
    return render_template('index.html',form=form)
    '''

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found"