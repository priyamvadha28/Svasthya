from flask import Flask, request, render_template, redirect, url_for, request, jsonify
from flask_pymongo import PyMongo
from math import radians, sin, cos, sqrt, atan2


app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://Healthcare:svasthya@cluster0.n6qsfnz.mongodb.net/Helathcare'

mongo = PyMongo(app)

pharmacies_collection = mongo.db.pharmacies

locations = [
    {'name': 'Praveena Hospital', 'lat': 12.79288551575399, 'lng': 80.22096888910694},
    {'name': 'Chettinad Hospital', 'lat': 12.799407667894487 , 'lng': 80.21719227733956},
    {'name': 'Dilip Multi Speciality Hospital', 'lat': 12.742826561359013, 'lng': 80.19436077266634},
    {'name': 'Swaram Hospital', 'lat': 12.788538396011399, 'lng': 80.22098467895333}]

api_key = 'AIzaSyAIuFz3oQQTp4lwGYGRwBnztgAQw_nszK0'

# Initialize user location as None
user_lat = None
user_lng = None

def find_nearest_pharmacy(tablet_name, user_lat, user_lng):
    nearest_pharmacy = None
    min_distance = float("inf")

    for pharmacy in pharmacies_collection.find({"inventory.medicine.name": tablet_name}):
        pharmacy_location = pharmacy["location"]
        pharmacy_lat = float(str(pharmacy_location[0]))  # Convert Decimal128 to float
        pharmacy_lng = float(str(pharmacy_location[1]))  # Convert Decimal128 to float

        # Calculate distance using Haversine formula
        distance = haversine(user_lat, user_lng, pharmacy_lat, pharmacy_lng)

        if distance < min_distance:
            min_distance = distance
            nearest_pharmacy = {
                "name": pharmacy["name"],
                "description": pharmacy["inventory"][0]["medicine"]["description"],
                "manufacturer": pharmacy["inventory"][0]["medicine"]["manufacturer"],
                "price": pharmacy["inventory"][0]["medicine"]["price"]
            }

    return nearest_pharmacy

@app.route('/find_nearest_location', methods=['POST'])
def find_nearest_location():
    try:
        lat = float(request.form['lat'])
        lng = float(request.form['lng'])

        # Calculate distances and find the nearest location
        nearest_location = None
        min_distance = float('inf')  # Initialize with a large value

        for location in locations:
            location_lat = location['lat']
            location_lng = location['lng']

            # Calculate distance using Haversine formula
            distance = haversine(lat, lng, location_lat, location_lng)

            if distance < min_distance:
                min_distance = distance
                nearest_location = location

        if nearest_location:
            return jsonify({'location': nearest_location['name'], 'distance': min_distance})
        else:
            return jsonify({'location': 'No results found'})

    except Exception as e:
        return jsonify({'error': str(e)})

def haversine(lat1, lon1, lat2, lon2):
    
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    # Choose the collection based on the role
    if role == 'patient':
        collection = mongo.db.patients
    elif role == 'doctor':
        collection = mongo.db.doctors
    elif role == 'hospital':
        collection = mongo.db.hospitals
    elif role == 'pharmacist':
        collection = mongo.db.pharmacists

    # Insert user details into the chosen collection
    collection.insert_one({'username': username, 'password': password})

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    # Choose the collection based on the role
    if role == 'patient':
        collection = mongo.db.patients
        redirect_page = 'patient_home.html'
    elif role == 'doctor':
        collection = mongo.db.doctors
        redirect_page = 'doctor_home.html'
    elif role == 'hospital':
        collection = mongo.db.hospitals
        redirect_page = 'hospital_home.html'
    elif role == 'pharmacist':
        collection = mongo.db.pharmacists
        redirect_page = 'pharmacist_home.html'
    else:
        # Handle an invalid or unknown role here
        return render_template('index.html')

    user = collection.find_one({'username': username, 'password': password})

    if user:
        # User authenticated successfully
        # Implement your authentication logic here
        return render_template(redirect_page)  # Redirect to the appropriate page

    # User authentication failed
    return render_template('index.html')

@app.route("/nearby_pharmacy", methods=["GET", "POST"])
def nearby_pharmacy():
    nearest_pharmacy = None

    global user_lat, user_lng

    if request.method == "POST":
        tablet_name = request.form["tablet_name"]
        nearest_pharmacy = find_nearest_pharmacy(tablet_name, user_lat, user_lng)

    return render_template("nearby_pharmacy.html", nearest_pharmacy=nearest_pharmacy)

@app.route('/patient_home.html')
def patient_home():
    # Add your logic for the patient home page here
    return render_template('patient_home.html')

@app.route('/learning.html')
def learning():
    # Add your logic for the patient home page here
    return render_template('learning_modules.html')

@app.route('/games')
def games():
    return render_template('quiz.html')

@app.route('/men_health')
def men_health():
    return render_template('quiz_men.html')

@app.route('/phy_health')
def phy_health():
    return render_template('quiz_phy.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

@app.route("/get_location", methods=["POST"])
def get_location():
    global user_lat, user_lng  

    if "latitude" in request.form and "longitude" in request.form:
        user_lat = float(request.form["latitude"])
        user_lng = float(request.form["longitude"])

    return jsonify({"message": "Location received."})

if __name__ == '__main__':
    app.run(debug=True)