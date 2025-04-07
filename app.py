from flask import Flask
from routes.events import events_bp

app = Flask(__name__)
app.register_blueprint(events_bp)

if __name__ == '__main__':
    app.run(debug=True)
