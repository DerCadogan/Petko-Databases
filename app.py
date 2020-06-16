from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test5.db'
db = SQLAlchemy(app)

class UserTable(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    FirstName = db.Column(db.String(200) )
    LastName = db.Column(db.String(200) )
    BirthDate = db.Column(db.String(200) )
    Country = db.Column(db.String(20) )
    City = db.Column(db.String(50) )
    PostalCode = db.Column(db.String(20) )
    Street = db.Column(db.String(200) )
    Email = db.Column(db.String(50) )

    def __repr__(self):
        return '<Your ID is %r>' % self.UserID


@app.route('/', methods=['POST', 'GET'])
def index():        
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        new_user = UserTable(FirstName = first_name, LastName = last_name)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/userprofile')
        except:
           return 'There was an issue adding the user'
    else:
        return render_template('index.html')


@app.route('/userprofile', methods=['POST', 'GET'])

def userprofile():

    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        birth_date = request.form['birthdate']
        country = request.form['country']
        city = request.form['city']
        postal_code = request.form['postalcode']
        street_nr = request.form['streetnr']
        e_mail = request.form['email']

        new_user = UserTable(FirstName = first_name, LastName = last_name, BirthDate = birth_date, Country = country, City = city, PostalCode = postal_code, Street = street_nr, Email = e_mail)

        try:
            db.session.add(new_user)
            db.session.commit()
            # return redirect('/userprofile')
            return render_template('UserProfile.html', user = new_user)
        except:
            return 'Issue'
    else:
        return render_template('UserProfile.html')

if __name__ == "__main__":
    app.run(debug=True)
