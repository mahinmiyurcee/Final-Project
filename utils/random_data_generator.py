import requests
import random

# URL of the local Flask app
url = "http://127.0.0.1:5000/"

# Function to generate random user data
def generate_random_user_data():
    age = random.randint(18, 65)  # Random age between 18 and 65
    gender = random.choice(['male', 'female', 'other'])
    income = random.randint(1000, 100000)  # Random income
    expenses = {
        'utilities': random.randint(0, 1000),
        'entertainment': random.randint(0, 1000),
        'school_fees': random.randint(0, 1000),
        'shopping': random.randint(0, 1000),
        'healthcare': random.randint(0, 1000)
    }
    return age, gender, income, expenses

# Automate form submission for 50 users
for i in range(50):
    # Generate random user data
    age, gender, income, expenses = generate_random_user_data()
    
    # Prepare the data for the POST request
    data = {
        'age': age,
        'gender': gender,
        'income': income,
        'utilities_check': expenses['utilities'] > 0,
        'utilities': expenses['utilities'] if expenses['utilities'] > 0 else '',
        'entertainment_check': expenses['entertainment'] > 0,
        'entertainment': expenses['entertainment'] if expenses['entertainment'] > 0 else '',
        'school_fees_check': expenses['school_fees'] > 0,
        'school_fees': expenses['school_fees'] if expenses['school_fees'] > 0 else '',
        'shopping_check': expenses['shopping'] > 0,
        'shopping': expenses['shopping'] if expenses['shopping'] > 0 else '',
        'healthcare_check': expenses['healthcare'] > 0,
        'healthcare': expenses['healthcare'] if expenses['healthcare'] > 0 else ''
    }
    
    # Send a POST request to submit the form
    response = requests.post(url, data=data)
    
    # Check if the request was successful
    if response.status_code == 302:  # Typically, a redirect on success
        print(f"User {i + 1} submitted successfully.")
    else:
        print(f"Failed to submit user {i + 1}: {response.status_code}")

print("All submissions attempted.")
