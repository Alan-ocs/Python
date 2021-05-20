import boto3
iam = boto3.client('iam')
import csv
  

filename = "file.csv"
  

fields = []
rows = []
  

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
      
    fields = next(csvreader)
  
    for row in csvreader:
        rows.append(row)

        iam.create_user(UserName=row[0])

        response = iam.create_login_profile(
            UserName=row[0],
            Password='MeMudar12345!',
            PasswordResetRequired=True
        )

        response = iam.add_user_to_group(
            GroupName=row[1],
            UserName=row[0]
        )