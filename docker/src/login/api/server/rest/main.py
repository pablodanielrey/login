from flask import Flask
from login.api.server.rest import login

def main():
    app = Flask(__name__)
    login.registerApi(app)
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    main()
