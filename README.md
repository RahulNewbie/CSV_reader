**CSV Reader**

**Requirement**

Flask, request, logging, json, csv, sqlite3 

Please use pip to install dependencies


**Installation**

For db_operation.py(without flask app), use "python db_operation.py" and it will read all the data from CSV file and 
insert records into sqlite database. Please put the CSV file in teh samee directory or specify the path in code

In code, i have created a sqlite file based database. Please change it into different folder

For Flask app:

It can run in 2 ways:

Go to the respective directory and use python command to run the file ( python backend_app.py)

 * Serving Flask app "backend_app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 
second way:

Use "export FLASK_APP=backend_app.py" and type "python -m flask run"


**Testing**

1. curl msg to list down all records:

	curl -X GET http://localhost:8000/data/

2. curl msg to get single record using it's id:

	curl -X GET http://localhost:8000/data/37889

Here last accessed timestamp for the specific record will be shown

Alternatively, write in browser the follwing urlhttp

1. To list down all records from database:

http://localhost:8000/data/   

2. To get single record for specified id:

http://localhost:8000/data/37889





