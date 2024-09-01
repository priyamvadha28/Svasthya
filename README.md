# Svasthya
Svasthya is a web-based healthcare platform designed to bridge the gap between healthcare services and rural populations. The platform connects users with local pharmacies, provides role-based access for patients, doctors, hospitals, and pharmacists, and offers essential healthcare information and services. It includes features for finding nearby pharmacies, managing user roles, and accessing healthcare modules and quizzes.

Features:
- Pharmacy Locator: Find the nearest pharmacy based on user location and available medicine.
- Role-Based Access: Different interfaces for patients, doctors, hospitals, and pharmacists.
- Healthcare Modules: Access educational modules and quizzes related to healthcare.
- User Authentication: Secure signup and login for different user roles.
- Location-Based Services: Calculate distances to nearby hospitals and pharmacies using the Haversine formula.

Setup:

Prerequisites:
- Python 3.x
- Flask
- Flask-PyMongo
- MongoDB instance (e.g., MongoDB Atlas)

Installation:
1. Clone the repository:
  git clone https://github.com/your-repo/svasthya.git
  cd svasthya

2. Install the required Python packages:
  pip install -r requirements.txt

3. Configure MongoDB: Update the app.config['MONGO_URI'] in app.py with your MongoDB connection string.

4. Run the Flask application:
  python app.py

5. Access the application: Open your web browser and go to http://127.0.0.1:5000/.

Usage:

1. Homepage: The homepage (/) provides access to all major functionalities of the platform.
2. Signup/Login: Users can sign up or log in with their roles (patient, doctor, hospital, pharmacist) to access role-specific pages.
3. Find Nearest Pharmacy: Use the /nearby_pharmacy endpoint to find the nearest pharmacy based on the medicine and user location.
4. Patient Home: Access patient-specific features and modules via /patient_home.html.
5. Healthcare Modules and Quizzes: Access educational content and quizzes through /learning.html, /games, /men_health, and /phy_health.
6. Logout: Users can log out and return to the homepage using the /logout endpoint.
