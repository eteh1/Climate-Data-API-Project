from flask import Flask, jsonify
from flask_restful import Api, Resource

# Initialize the Flask app and API
app = Flask(__name__)
api = Api(app)

class ClimateData(Resource):
    def get(self):
        # Return the last 5 climate data points (example)
        data = cleaned_data.to_dict(orient='records')
        return jsonify(data)

api.add_resource(ClimateData, '/climate_data')

if __name__ == '__main__':
    app.run(debug=True)
