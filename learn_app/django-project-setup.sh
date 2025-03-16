# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
# venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install django djongo psycopg2-binary pymongo django-bootstrap4

# Create Django project
django-admin startproject mywebsite

# Navigate to project
cd mywebsite

# Create a main app
python manage.py startapp main_app
