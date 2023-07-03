# Lambda 2 does select on the db
import pg8000.native
import json

r = [
        3,
        "2023-07-02 16:35:54.568529",
        "luz",
        56.0,
        False
    ]

def map_to_dict(rows):

    keys = ['id', 'fecha', 'sensor', 'value', 'error']

    d = []
    for i in range(len(rows)):
        d2 = {}
        for j in range(len(rows[i])):
            d2[keys[j]] = rows[i][j]
        d.append(d2)
    return d


def lambda_handler(event, context):

    body = json.loads(event['body'])
    headers = event['headers']
    if 'usm' not in headers:
        return {
            'statusCode': 418,
            'body': 'rtfm'
        }
    if headers['usm'] != 'TallerDeProgra':
        return {
            'statusCode': 418,
            'body': 'rtfm'
        }

    # check if request is in the body
    if 'sensor' not in body:
        return {
            'statusCode': 400,
            'body': 'Missing Parameters'
        }

    # Connect to an existing database
    with pg8000.native.Connection(host="database-2.c1doqm3wbuwt.us-east-2.rds.amazonaws.com", user="postgres", password="postgres", database="main") as conn:

        response = conn.run("select * from logs where sensor = :sensor", sensor=body['sensor'])
        response = map_to_dict(response)
        
    return {
        'statusCode': 200,
        'body': json.dumps(response, default=str)
    }
