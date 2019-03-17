from flask_restplus import Namespace, fields


class ItemDto:
    api = Namespace('item', description='item related operations')
    item = api.model('item', {
        'number_1': fields.String(required=True, description='item number_1'),
        'number_2': fields.String(required=True, description='item number_2')
    })


