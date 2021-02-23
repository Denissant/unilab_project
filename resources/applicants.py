from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.applicants import ItemModel
from modules.parsing import cv_parse


class ItemList(Resource):
    def get(self):
        all_items = ItemModel.cv_list()
        if all_items:
            return all_items, 200
        else:
            return "Data not found", 404

    @jwt_required()
    def delete(self):
        all_items = ItemModel.query.all()
        for i in all_items:
            i.del_from_db()
        return {"message": "Database successfully cleared"}, 200


class Item(Resource):
    item_parser = reqparse.RequestParser()
    item_parser.add_argument('name',
                             type=str,
                             required=True,
                             help='"name" is required and should be string type')
    item_parser.add_argument('sex',
                             type=str,
                             required=True,
                             help='"sex" is required and should be float type')
    item_parser.add_argument('age',
                             type=int,
                             required=True,
                             help='"type" is required and should be string type')
    item_parser.add_argument('last_company',
                             type=str,
                             required=True,
                             help='"experience" is required and should be string type')
    item_parser.add_argument('last_position',
                             type=str,
                             required=True,
                             help='"name" is required and should be string type')
    item_parser.add_argument('relevant_experience',
                             type=int,
                             required=True,
                             help='"sex" is required and should be float type')
    item_parser.add_argument('school_diploma',
                             type=int,
                             required=True,
                             help='"type" is required and should be string type')
    item_parser.add_argument('bachelors_degree',
                             type=int,
                             required=True,
                             help='"name" is required and should be string type')
    item_parser.add_argument('bachelors_uni_faculty',
                             type=str,
                             required=True,
                             help='"sex" is required and should be float type')
    item_parser.add_argument('driving_license',
                             type=int,
                             required=True,
                             help='"type" is required and should be string type')
    item_parser.add_argument('skills_and_qualities',
                             type=str,
                             required=True,
                             help='"sex" is required and should be float type')
    item_parser.add_argument('english_level',
                             type=int,
                             required=True,
                             help='"type" is required and should be string type')

    def get(self, link_id):
        item = ItemModel.find_by_name(link_id)
        if item:
            return {"message": f'requested CV: {item.json()}'}, 200
        return f'{link_id} not found', 404

    @jwt_required()
    def post(self, link_id):
        received_data = Item.item_parser.parse_args()
        received_data = cv_parse(received_data)

        try:
            item = ItemModel.find_by_name(received_data['name'])
            if item:
                return {"error_message": "There's someone with the same name. Please enter a number after your name (e.g. John Smith 2)"}, 400

        finally:
            item = ItemModel(**received_data)
            try:
                item.save_to_db()
                return {"message": f'successfully added: {received_data}'}, 200
            except:
                return {"error_message": "SQLAlchemy error. Try using a unique name"}, 400

    @jwt_required()
    def put(self, link_id):
        try:
            received_data = Item.item_parser.parse_args()
            received_data = cv_parse(received_data)
            item = ItemModel.find_by_name(received_data['name'])

            if item:
                item.del_from_db()
            item = ItemModel(**received_data)
            item.save_to_db()
            return {"message": f'successfully updated or added: received_data'}, 200
        except:
            return {'error_message': 'SQLAlchemy error'}, 400

    @jwt_required()
    def delete(self, link_id):
        try:
            item = ItemModel.find_by_name(link_id)
            if item:
                item.del_from_db()
                return {"message": f'successfully deleted: {item}'}, 200
        finally:
            return f'{link_id} not found', 404
