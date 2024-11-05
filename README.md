Tourist Destinations CRUD Web Application
This project is a web application designed to manage information about tourist destinations. It allows users to create, read, update, and delete (CRUD) entries for different tourist spots, including details like location, weather, and descriptions. The application provides an organized platform to explore and manage popular tourist destinations.

Features
Destination Management: Add, update, and delete tourist destination entries.
Detailed Information: Each entry includes place name, weather, location, Google Maps link, an image, and a description.
Search and Filter: Easily search for destinations and filter by location or other attributes.
Responsive Design: User-friendly and responsive layout for a seamless experience on different devices.
Technologies Used
Backend: Django REST Framework for API development.
Frontend: HTML templates with CSS for styling and Bootstrap for responsive design.
Database: MySQL or PostgreSQL for storing destination information.
Requirements
Python and Django for backend functionality.
MySQL or PostgreSQL database setup.
HTML/CSS with Bootstrap for frontend design.
Installation
Clone the repository:

git clone https://github.com/Rinsan-K/Tourist_Destinations.git
Navigate to the project directory:

cd Tourist_Destinations
Install dependencies:

pip install -r requirements.txt
Configure the database settings in settings.py.
Run migrations to set up the database:

python manage.py migrate
Start the development server:

python manage.py runserver
Usage
Access the web application at http://127.0.0.1:8000.
Use the web interface to add new tourist destinations, view detailed information, and perform search and filtering.
Manage destinations through the provided CRUD interface.
Project Structure
models/: Django models for managing destination data.
views/: Views to handle requests and render templates.
templates/: HTML templates for the frontend.
static/: Static assets such as CSS, JavaScript, and images.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request for new features or bug fixes.
