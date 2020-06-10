from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class UserTable(db.Model):
    UserID = db.Column(db.String(200), primary_key= True)
    FirstName = db.Column(db.String(200) )
    LastName = db.Column(db.String(200) )
    BirthDate = db.Column(db.DateTime )
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
        FirstName = request.form.get('firstname')
        Model_FirstName = UserTable(FirstName=FirstName)

        try:
            db.session.add(Model_FirstName)
            db.session.commit()
            return redirect('/')
        except:

            return 'There was an issue adding your task'

    else:
        #Page_FirstName = UserTable.query.order_by(FirstName.date_created).first()         
        return render_template('index.html')


@app.route('/delete/<int:id>')
def delete(id):
     task_to_delete = Todo.query.get_or_404(id)

     try:
         db.session.delete(task_to_delete)
         db.session.commit()
         return redirect('/')
     except:
         return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
     task = Todo.query.get_or_404(id)

     if request.method == 'POST':
         task.content = request.form.get['content']

         try:
             db.session.commit()
             return redirect('/')
         except:
             return 'There was an issue updating your task'

     else:
         return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
