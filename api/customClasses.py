import json
from django.http import JsonResponse
import string
import secrets
import random

class checkJson:

    def __init__(self):
        return None

    def isJson(self, json_file):
        try:
            json_object = json.loads(json_file)
        except ValueError as e:
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'Invalid Json File'
        return True
