import re

from flask_wtf import FlaskForm
from wtforms import (DateField, EmailField, FileField, FormField, HiddenField,
                     PasswordField, SelectField, StringField, SubmitField,
                     TextAreaField, TimeField, validators)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, Optional, Regexp, ValidationError)

from hris.models import *


class DeleteEmployeeModal(FlaskForm):
   delete = SubmitField(label='Delete')

class AccountForm(FlaskForm):
   image_path = FileField(label='Employee Picture', render_kw={'accept': 'image/*'}, validators=[Optional(), validators.regexp(u'([^\\s]+(\\.(?i)(jpe?g|png))$)')])
   old_password = PasswordField(label='Old Password', validators=[Length(min=8), Optional()])
   password1 = PasswordField(label='New Password', validators=[Length(min=8), Optional()])
   password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), Optional()])

class EmployeeForm(FlaskForm):
   def validate_email_address(self, email_address_to_check):
      email_address = Users.query.filter_by(company_email=email_address_to_check.data).first()
      if email_address:
         return True
        
   #Employee Account
   image_path = FileField(label='Employee Picture', render_kw={'accept': 'image/*'},validators=[Optional(), validators.regexp(u'([^\\s]+(\\.(?i)(jpe?g|png))$)')])
   company_email = EmailField(label='Company Email', validators=[DataRequired()])
   password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
   password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
   access = SelectField(label='Access', choices=[('admin', 'Admin'), ('employee', 'Employee')], 
   validators=[DataRequired()])

   #Employee Profile
   last_name = StringField(label='Last Name', validators=[DataRequired()])
   first_name = StringField(label='First Name', validators=[DataRequired()])
   middle_name = StringField(label='Middle Name', validators=[DataRequired()])
   gender = SelectField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
   validators=[DataRequired()])
   birth_date = StringField(label='Birth Date', validators=[DataRequired()])
   civil_status = SelectField(label='Civil Status', choices=[('single', 'Single'), ('married', 'Married'), 
   ('divorced', 'Divorced'), ('separated', 'Separated'), ('widowed', 'Widowed')], validators=[DataRequired()])
   mobile = StringField(label='Mobile Number', validators=[DataRequired()])
   email = EmailField(label='Email', validators=[Email(), DataRequired()])
   address = StringField(label='Address', validators=[DataRequired()])
   emergency_name = StringField(label='Contact Name', validators=[DataRequired()])
   emergency_contact = StringField(label='Contact Number', validators=[DataRequired()])
   emergency_relationship = StringField(label='Relationship', validators=[DataRequired()])
   tin = StringField(label='TIN', validators=[DataRequired(), Length(min=9, max=12)])
   sss = StringField(label='SSS', validators=[DataRequired(), Length(min=10, max=10)])
   phil_health = StringField(label='Philhealth', validators=[DataRequired(), Length(min=12, max=12)])
   pag_ibig = StringField(label='Pag-Ibig', validators=[DataRequired(), Length(min=12, max=12)])

   #Employment Info
   positions = SelectField(label='Position', coerce=int, validators=[DataRequired()])
   description = TextAreaField(label='Description')
   salary_rate = SelectField(label='Salary Rate', coerce=int, validators=[DataRequired()])
   start_date = StringField(label='Start Date', validators=[DataRequired()])
   end_date = StringField(label='End Date', render_kw={'disabled':True}, validators=[DataRequired()])
   status = SelectField(label='Status', choices=[('hired', 'Hired'), ('retired', 'Retired'), ('terminated', 'Terminated')], validators=[DataRequired()])