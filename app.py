from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://dbUser:GMZ9O1rhPQtaDBob@cluster0.drqaw.mongodb.net/survey_db?retryWrites=true&w=majority")
db = client.survey_db  # Create a database
collection = db.survey  # Create a collection

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        income = request.form['income']
        expenses = {}
        for category in ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']:
            if f'{category}_check' in request.form:
                expenses[category] = request.form[category]
            else:
                expenses[category] = '0'
        
        # Store in MongoDB
        user_data = {
            'age': age,
            'gender': gender,
            'income': income,
            'expenses': expenses
        }
        collection.insert_one(user_data)
        
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
