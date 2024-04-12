# Import Flask and create an instance of the application
from flask import Flask
app = Flask(__name__)

# Set the 'MONGODB_URI' configuration option
app.config['MONGODB_URI'] = 'mongodb://localhost:27017/mydatabase'

# Other configurations and code...

if __name__ == '__main__':
    app.run(debug=True)
