# SkillSwap

A Flask-based web application for skill exchange and learning community.

## Requirements

- Python 3.8+
- pip (Python package installer)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/skillswap-py.git
cd skillswap-py
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install required packages:
```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-login
pip install flask-migrate
pip install werkzeug
```

5. Initialize the database:
```bash
python create_tables.py
```

6. Run database migrations:
```bash
flask db upgrade
```

7. Start the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Features

- User authentication (register, login, logout)
- Password reset functionality
- User dashboard
- Skill matching system
- Session scheduling

## Project Structure

```
skillswap-py/
├── app.py              # Main application file
├── models.py           # Database models
├── create_tables.py    # Database initialization
├── static/            
│   └── style.css      # CSS styles
├── templates/          # HTML templates
├── migrations/         # Database migrations
└── README.md
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.