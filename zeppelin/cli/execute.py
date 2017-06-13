import requests
import os
import argparse
import json


def execute_notebook(notebook_id):
    r = requests.post('http://localhost:8080/api/notebook/job/' + notebook_id)
    print(r.json())
    r = requests.get('http://localhost:8080/api/notebook/' + notebook_id)
    if r.status_code == 200:
        body = r.json()['body']

        for paragraph in body['paragraphs']:
            if paragraph['status'] == 'ERROR':
                print (paragraph['errorMessage'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='path_to_notebook_json', required=True,
                        help='Zeppelin notebook input file (.json)')
    parser.add_argument('-p', dest='output_path',
                        help='Path to save notebook output (optional)')
    args = parser.parse_args()

    with open(args.path_to_notebook_json, 'rb') as notebook:
        try:
            t = json.load(notebook)
            notebook_id = args.path_to_notebook_json.split('/')[-2]
            print(notebook_id)
            execute_notebook(notebook_id)
        except ValueError:
            print('ERROR: Invalid JSON format')
            sys.exit(1)

if __name__ == '__main__':
    main()
