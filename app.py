# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import os
import requests

# Initialize Flask application
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
# Generate a random secret key for session security
app.config['SECRET_KEY'] = os.urandom(24)
# Set the base URL for the external API
app.config['API_BASE_URL'] = 'http://127.0.0.1:8000'

# Home route - requires authentication
@app.route('/')
def index():
    # Check if user is authenticated by verifying access token
    if not session.get('access_token'):
        return redirect(url_for('login'))
    return render_template('index.html')

# Login route - handles both GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Redirect to home if already authenticated
    if session.get('access_token'):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            # Prepare login credentials from form data
            login_data = {
                "username": request.form.get('username'),
                "password": request.form.get('password')
            }

            # Make API call to authenticate user
            response = requests.post(
                f"{app.config['API_BASE_URL']}/api/users/login/",
                json=login_data
            )

            if response.status_code == 200:
                # Store authentication tokens in session
                session['access_token'] = response.json()['access']
                session['refresh_token'] = response.json()['refresh']
                return redirect(url_for('index'))
            else:
                # Handle authentication failure
                error_message = response.json().get('detail', 'Invalid username or password')
                flash(error_message)
                return redirect(url_for('login'))

        except requests.exceptions.RequestException as e:
            # Handle API connection errors
            flash('Error connecting to the server')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Signup route - handles user registration
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Redirect to home if already authenticated
    if session.get('access_token'):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            # Prepare registration data from form
            registration_data = {
                "username": request.form.get('username'),
                "email": request.form.get('email'),
                "password": request.form.get('password'),
                "password2": request.form.get('password2'),
                "first_name": request.form.get('firstname'),
                "last_name": request.form.get('lastname')
            }

            # Make API call to register new user
            response = requests.post(
                f"{app.config['API_BASE_URL']}/api/users/register/",
                json=registration_data
            )

            if response.status_code == 201:
                # Store authentication tokens in session
                session['access_token'] = response.json()['access']
                session['refresh_token'] = response.json()['refresh']

                # Initialize user profile after successful registration
                profile_response = requests.post(
                    f"{app.config['API_BASE_URL']}/api/users/profile/",
                    headers={'Authorization': f"Bearer {session['access_token']}"}
                )

                if profile_response.status_code == 201:
                    return redirect(url_for('index'))
                else:
                    flash('Error initializing user profile')
                    return redirect(url_for('signup'))

            else:
                # Handle registration failure
                error_message = response.json().get('detail', 'Registration failed')
                flash(error_message)
                return redirect(url_for('signup'))

        except requests.exceptions.RequestException as e:
            # Handle API connection errors
            flash('Error connecting to the server')
            return redirect(url_for('signup'))
    
    return render_template('signup.html')

# Logout route - handles user logout
@app.route('/logout')
def logout():
    try:
        # Call API to invalidate tokens
        requests.post(
            f"{app.config['API_BASE_URL']}/api/users/logout/",
            headers={'Authorization': f"Bearer {session.get('access_token')}"}
        )
    except:
        # Ignore API errors during logout
        pass
    
    # Clear session data
    session.clear()
    return redirect(url_for('login'))

# Discover route - requires authentication
@app.route('/discover', methods=['GET', 'POST'])
def discover():
    # Check if user is authenticated
    if not session.get('access_token'):
        return redirect(url_for('login'))
    return render_template('discover.html')

@app.route('/profile')
def profile():
    access_token = session.get('access_token', '')
    return render_template('profile.html', access_token=access_token)

@app.route('/chat', methods=['GET'])
def chat():
    if not session.get('access_token'):
        return redirect(url_for('login'))
    return render_template('chat.html')

@app.route('/michaelChen', methods=['GET'])
def michaelChen():
    if not session.get('access_token'):
        return redirect(url_for('login'))
    return render_template('michaelChen.html')

@app.route('/project')
def project():
    access_token = session.get('access_token', '')
    return render_template('project.html', access_token=access_token)


# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
