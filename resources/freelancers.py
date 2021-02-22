from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.freelancers import ItemModel


class ItemList(Resource):
    def get(self):
        all_items = ItemModel.query.all()
        if all_items:
            return all, 200
        else:
            return "Data not found", 404

    @jwt_required()
    def delete(self):
        all_items = ItemModel.query.all()
        for i in all_items:
            i.del_from_db()
        return "Database successfully cleared", 200


class Item(Resource):
    item_parser = reqparse.RequestParser()
    item_parser.add_argument('nickname',
                             type=str,
                             required=True,
                             help='"nickname" is required and should be string type')
    item_parser.add_argument('hourly_wage',
                             type=float,
                             required=True,
                             help='"hourly_wage" is required and should be float type')
    item_parser.add_argument('type',
                             type=str,
                             required=True,
                             help='"type" is required and should be string type')
    item_parser.add_argument('experience',
                             type=str,
                             required=True,
                             help='"experience" is required and should be string type')

    def get(self, link_id):
        item = ItemModel.find_by_name(link_id)
        if item:
            display_string = f"""<h2>{item['nickname']}'s Profile: </h2>\
            Hourly Wage: ${item['hourly_wage']} <br>\
            Type: {item['type']} <br>\
            Experience: {item['experience']} <br> """
            return display_string, 200
        else:
            return f'{link_id} not found', 404

    @jwt_required()
    def post(self, link_id):
        item = ItemModel.find_by_name(link_id)
        if item:
            return f"""Nickname "{item.nickname}" is already used""", 400
        else:
            received_data = Item.item_parser.parse_args()
            item = ItemModel(1, **received_data)    # id should be fixed

            item.save_to_db()
            return {"message": f'added {received_data}'}, 200

    @jwt_required()
    def put(self, link_id):
        item = ItemModel.find_by_name(link_id)
        received_data = Item.item_parser.parse_args()

        if item:
            item.hourly_wage = received_data['hourly_wage']
            item.type = received_data['type']
            item.experience = received_data['experience']
        else:
            item = ItemModel(1, **received_data)    # id should be fixed
        print(item)
        item.save_to_db()
        return received_data, 200

    @jwt_required()
    def delete(self, link_id):
        item = ItemModel.find_by_name(link_id)
        if item:
            item.del_from_db()
            return f'deleted: {item}', 200
        else:
            return f'{link_id} not found', 404
