from datetime import datetime

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, URL
import csv
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class JobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    organization = StringField('Organization', validators=[DataRequired()])
    application_submit_date = DateField('Application Submit Date eg 2005-05-28', format='%Y-%m-%d', validators=[DataRequired()],
                                        default=datetime.now())
    last_update_date = DateField('Last Application Update Date eg 2007-02-21', format='%Y-%m-%d', validators=[DataRequired()],
                                 default=datetime.now())
    resume = StringField('Resume Used (URL)',
                         validators=[DataRequired(), URL(require_tld=True, message='Enter a valid URL')])
    cover_letter = StringField('Cover Letter Used (URL)',
                               validators=[DataRequired(), URL(require_tld=True, message='Enter a valid URL')])
    status = SelectField('Application Status', choices=[('Choose a Option..'),('Applied'), ('Interview'), ('Awaiting'), ('Rejected'), ('Employed')],
                         validators=[DataRequired()])
    comments = TextAreaField('Comments')
    company_review = SelectField('Company Rating', choices=[('Choose a Option..'),('✘'), ('✘✘'), ('✘✘✘'), ('✘✘✘✘'), ('✘✘✘✘✘')],
                                 validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        title = request.form['title']
        organization = request.form['organization']
        application_submit_date = request.form['application_submit_date']
        last_update_date = request.form['last_update_date']
        resume = request.form['resume']
        cover_letter = request.form['cover_letter']
        status = request.form['status']
        comments = request.form['comments']
        company_review = request.form['company_review']
        fieldnames = [
            title, organization, application_submit_date, resume, cover_letter,
            last_update_date, status, comments, company_review
        ]
        with open('title-data.csv', 'a', encoding="utf8", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(fieldnames)
        return render_template('add.html', form=JobForm(formdata=None))
    # Exercise:
    # Make the form write a new row into title-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/applications', methods=["GET", "POST"])
def jobs():
    with open('job_listings.csv', encoding="utf8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('applications.html', jobs=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
