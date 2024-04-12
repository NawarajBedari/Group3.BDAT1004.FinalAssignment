from flask import Flask
from database.mongodb_connector import get_mongo_collection
from api.data_transformer import data_transformer_app
from visualization.chart_generator import visualization_app

app = Flask(__name__)

# Set the 'MONGODB_URI' configuration option
app.config['MONGODB_URI'] = 'mongodb://localhost:27017/mydatabase'

# Set the 'collection' attribute on the app config
app.config['collection'] = get_mongo_collection(app.config['MONGODB_URI'])

# Register blueprints
app.register_blueprint(data_transformer_app)
app.register_blueprint(visualization_app)

if __name__ == '__main__':
    app.run(debug=True)
