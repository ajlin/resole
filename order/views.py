from flask-uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import PasswordField, StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

photos = UploadSet('photos', IMAGES)
configure_uploads(app,photos)


class OrderForm(FlaskForm):
    first = StringField('Username',
                        validators=[DataRequired()]
                        )
    last = PasswordField('Password',
                         validators=[DataRequired()]
                         )
    email = StringField('Email',
                        validators = [DataRequired(), Email()]
                        )
    quote = BooleanField('Quote Requested')
    '''
    photo = FileField('Photo Upload',
                      validators = [FileAllowed(photos, "Images only!")])
    '''
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def order():
    form = OrderForm()

    '''
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None
        
    return render_template('index.html', form=form, file_url=file_url)
    '''
    return render_template('index.html', form=form)