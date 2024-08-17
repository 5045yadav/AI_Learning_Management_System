from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import Config

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Database connection
db = mysql.connector.connect(
    host=app.config['DB_HOST'],
    user=app.config['DB_USER'],
    password=app.config['DB_PASSWORD'],
    database=app.config['DB_NAME']
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Handle profile form submission
        student_id = request.form['student_id']
        preferences = request.form['preferences']
        performance_data = request.form['performance_data']

        # Save to database
        cursor.execute("INSERT INTO profiles (student_id, preferences, performance_data) VALUES (%s, %s, %s)",
                       (student_id, preferences, performance_data))
        db.commit()

        return redirect(url_for('index'))
    return render_template('student_profile.html')

@app.route('/learning-module', methods=['GET'])
def learning_module():
    # Fetch learning content based on student profile
    return render_template('learning_module.html')

if __name__ == '__main__':
    app.run(debug=True)

