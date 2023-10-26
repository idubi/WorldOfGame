from flask import Blueprint, request
from server.main_score import score_server


# Create a Blueprint instance
main = Blueprint('main', __name__)


@main.route('/',methods=['GET'])
def index():
    return '<p>Hello from the score server , world of games - level 3 ! </p>' \
            '<p> all apis are on <b>/api/v1 </b> base route</p>'

@main.route('/score',methods=['GET'])
def score():
    user_name = request.args.get('user_name')
    return score_server(user_name)
    
    
