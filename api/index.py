from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
from data import restaurants, details, menus
from datetime import datetime
import uuid

app = Flask(__name__)
api = Api(app)

class RestaurantList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(restaurants),
            "restaurants": restaurants
        }

class RestaurantDetail(Resource):
    def get(self, restaurant_id):
        if restaurant_id in details:
            return {
                "error": False,
                "message": "success",
                "restaurant": details[restaurant_id]
            }
        return {"error": True, "message": "Restaurant not found"}, 404

class RestaurantSearch(Resource):
    def get(self):
        query = request.args.get('q', '').lower()
        result = [r for r in restaurants if query in r['name'].lower() or query in r['description'].lower()]
        return {
            "error": False,
            "founded": len(result),
            "restaurants": result
        }

class AddReview(Resource):
    def post(self):
        data = request.get_json()
        restaurant_id = data.get('id')
        name = data.get('name')
        review = data.get('review')
        photo = data.get('photo')
        
        if restaurant_id in details:
            new_review = {
                "review_id": str(uuid.uuid4()),
                "name": name,
                "review": review,
                "photo": photo,
                "date": datetime.now().strftime("%d %B %Y")
            }
            details[restaurant_id]['customerReviews'].append(new_review)
            return {
                "error": False,
                "message": "success",
                "customerReviews": details[restaurant_id]['customerReviews']
            }
        return {"error": True, "message": "Restaurant not found"}, 404

class UpdateReview(Resource):
    def put(self):
        data = request.get_json()
        restaurant_id = data.get('id')
        review_id = data.get('review_id')
        new_review_text = data.get('review')
        
        if restaurant_id in details:
            reviews = details[restaurant_id]['customerReviews']
            review_to_update = next((r for r in reviews if r['review_id'] == review_id), None)
            if review_to_update:
                review_to_update['review'] = new_review_text
                review_to_update['date'] = datetime.now().strftime("%d %B %Y")
                return {
                    "error": False,
                    "message": "success",
                    "customerReviews": reviews
                }
            return {"error": True, "message": "Review not found"}, 404
        return {"error": True, "message": "Restaurant not found"}, 404

class DeleteReview(Resource):
    def delete(self):
        data = request.get_json()
        restaurant_id = data.get('id')
        review_id = data.get('review_id')
        
        if restaurant_id in details:
            reviews = details[restaurant_id]['customerReviews']
            review_to_delete = next((r for r in reviews if r['review_id'] == review_id), None)
            if review_to_delete:
                reviews.remove(review_to_delete)
                return {
                    "error": False,
                    "message": "success",
                    "customerReviews": reviews
                }
            return {"error": True, "message": "Review not found"}, 404
        return {"error": True, "message": "Restaurant not found"}, 404

class Menu(Resource):
    def get(self, restaurant_id):
        if restaurant_id in menus:
            return {
                "error": False,
                "message": "success",
                "menu": menus[restaurant_id]
            }
        return {"error": True, "message": "Menu not found"}, 404

class ReserveTable(Resource):
    def post(self):
        data = request.get_json()
        restaurant_id = data.get('restaurant_id')
        customer_name = data.get('customer_name')
        reservation_time = data.get('reservation_time')
        
        if restaurant_id in details:
            new_reservation = {
                "reservation_id": str(uuid.uuid4()),
                "customer_name": customer_name,
                "reservation_time": reservation_time,
                "date": datetime.now().strftime("%d %B %Y")
            }
            if 'reservations' not in details[restaurant_id]:
                details[restaurant_id]['reservations'] = []
            details[restaurant_id]['reservations'].append(new_reservation)
            return {
                "error": False,
                "message": "success",
                "reservations": details[restaurant_id]['reservations']
            }
        return {"error": True, "message": "Restaurant not found"}, 404

class RateRestaurant(Resource):
    def post(self):
        data = request.get_json()
        restaurant_id = data.get('restaurant_id')
        rating = data.get('rating')
        
        if restaurant_id in details:
            if 'ratings' not in details[restaurant_id]:
                details[restaurant_id]['ratings'] = []
            details[restaurant_id]['ratings'].append(rating)
            average_rating = sum(details[restaurant_id]['ratings']) / len(details[restaurant_id]['ratings'])
            return {
                "error": False,
                "message": "success",
                "average_rating": average_rating
            }
        return {"error": True, "message": "Restaurant not found"}, 404

api.add_resource(RestaurantList, '/list')
api.add_resource(RestaurantDetail, '/detail/<string:restaurant_id>')
api.add_resource(RestaurantSearch, '/search')
api.add_resource(AddReview, '/review')
api.add_resource(UpdateReview, '/review/update')
api.add_resource(DeleteReview, '/review/delete')
api.add_resource(Menu, '/menu/<string:restaurant_id>')
api.add_resource(ReserveTable, '/reserve')
api.add_resource(RateRestaurant, '/rate')

def handler(request, context):
    return app(request.environ, context.start_response)
