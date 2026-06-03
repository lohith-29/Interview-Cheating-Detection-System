from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.video_routes import video_bp
from routes.report_routes import report_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(video_bp)
app.register_blueprint(report_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)