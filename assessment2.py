import json
import requests

def retrieveData():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    #200 means status OK
    if response.status_code == 200:
        print("Successful Retrieval")
        return response.json()

    else:
        print("There was an error with retrieving the data." + response.status_code)


def lambda_handler(event, context):
    # TODO implement
    authors = retrieveData()
    return {
        'statusCode': 200,
        'body': json.dumps(authors)
    }   