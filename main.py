from flask import Flask
from app.order_service import bp as order_bp
from app.report_endpoint import bp as debug_bp

app = Flask(__name__)
app.register_blueprint(order_bp)
app.register_blueprint(debug_bp)

if __name__ == "__main__":
    app.run(port=5000)
