from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

## Main Flask application
## Configuration of the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
#########################
# Set up a route for users to 
#
#
#######################
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get user input from the form
        user_name = request.form['user_name']

        # Create a new User instance
        new_user = User(name=user_name)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect('/')  # Redirect to the index page after adding the user

    return render_template('add_user.html')


if __name__ == '__main__':
    app.run()