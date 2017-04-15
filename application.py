# run.py is our main entry point for the application. "python run.py" starts the server

from app import application

if __name__ == '__main__':
    application.run(host="0.0.0.00", debug=True)
