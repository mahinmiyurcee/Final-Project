import csv
from pymongo import MongoClient

class User:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.survey_db
        self.collection = self.db.survey
    
    def export_to_csv(self, filename='user_data.csv'):
        users = self.collection.find()
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['age', 'gender', 'income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for user in users:
                writer.writerow({
                    'age': user['age'],
                    'gender': user['gender'],
                    'income': user['income'],
                    'utilities': user['expenses']['utilities'],
                    'entertainment': user['expenses']['entertainment'],
                    'school_fees': user['expenses']['school_fees'],
                    'shopping': user['expenses']['shopping'],
                    'healthcare': user['expenses']['healthcare']
                })

# Usage
user_processor = User()
user_processor.export_to_csv()