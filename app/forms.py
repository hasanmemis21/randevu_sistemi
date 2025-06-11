from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    submit = SubmitField('Giriş Yap')

class AppointmentForm(FlaskForm):
    date = DateField('Tarih', validators=[DataRequired()], format='%Y-%m-%d')
    time = TimeField('Saat', validators=[DataRequired()])
    message = TextAreaField('Mesaj', validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField('Randevu Talebi Gönder')
