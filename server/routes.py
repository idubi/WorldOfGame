from flask import Blueprint, request
from server.main_score import score_server


# Create a Blueprint instance
main = Blueprint('main', __name__)


@main.route('/',methods=['GET'])
def index():
    return '<p>Hello from the score server , world of games - level 5 ! </p>' \
            '<p> all apis are on  base route</p>'

@main.route('/score',methods=['GET'])
def score():
    user_name = request.args.get('user_name')
    return score_server(user_name)
    
    
