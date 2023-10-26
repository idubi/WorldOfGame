from flask import Flask
from flask_cors import CORS
from server import routes





def execute_flask(port=30000, api_rout='/api/v1'):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    # Register the blueprint with the app
    app.register_blueprint(routes.main, url_prefix=f'{api_rout}/')
    
    app.run(port=port)
    
    
execute_flask(port=30000,api_rout='')

 
