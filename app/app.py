from flask import Flask, jsonify
from health import health_bp

app = Flask(__name__)

# Register health routes
#aadded new commnent
app.register_blueprint(health_bp)


@app.route("/api/orders", methods=["GET"])
def orders():
    return jsonify({
        "orders": [
            {
                "id": 1001,
                "item": "Laptop",
                "quantity": 1
            },
            {
                "id": 1002,
                "item": "Monitor",
                "quantity": 2
            }
        ]
    })


@app.route("/api/customers", methods=["GET"])
def customers():
    return jsonify({
        "customers": 25
    })


@app.route("/api/version", methods=["GET"])
def version():
    return jsonify({
        "application": "resilience-framework-demo",
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )