import uuid
import datetime

def save_new_item(data):

    response_object = {
            'result': '3'
    }
    return response_object, 201


def get_all_items():
    response_object = {
            'number_1': '1',
            'number_2': '2'
    }
    return response_object, 200



