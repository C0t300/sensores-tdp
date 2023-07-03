# Lambda 1 does insertions into the DBs
import pg8000.native
import json

def lambda_handler(event, context):

    body = json.loads(event['body'])

    # check if values are in the body
    check = ['date', 'sensor', 'value'] #'error' is optional as it is inserted as false by default
    for key in check:
        if key not in body:
            return {
                'statusCode': 400,
                'body': 'Missing Parameters'
            }

    # Connect to an existing database
    with pg8000.native.Connection(host="database-2.c1doqm3wbuwt.us-east-2.rds.amazonaws.com", user="postgres", password="postgres", database="main") as conn:

        # Open a cursor to perform database operations
        if 'error' in body:
            conn.run("INSERT INTO logs (date, sensor, value, error) VALUES (:date, :sensor, :value, :error)", date=body['date'], sensor=body['sensor'], value=body['value'], error=body['error'])
        else:
            conn.run("INSERT INTO logs (date, sensor, value) VALUES (:date, :sensor, :value)", date=body['date'], sensor=body['sensor'], value=body['value'])
        #conn.commit()
        
    return {
        'statusCode': 200,
        'body': 'Success'
    }
