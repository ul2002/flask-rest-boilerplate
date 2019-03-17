from flask import request
from flask_restplus import Resource

from ..util.dto import ItemDto
from ..service.item_service import save_new_item, get_all_items

api = ItemDto.api
_item = ItemDto.item


@api.route('/')
class ItemList(Resource):
    @api.doc('list_of_item')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        """List all Item"""
        return get_all_items()

    @api.expect(_item, validate=True)
    @api.response(201, 'Item successfully created.')
    @api.doc('create a new Item')
    def post(self):
        """Creates a new Items """
        data = request.json
        return save_new_item(data=data)



