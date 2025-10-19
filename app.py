from flask import Flask, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

# Apply ProxyFix to respect X-Forwarded headers from Apache
app = Flask(__name__, static_folder="public", static_url_path="/public")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_prefix=1)

@app.get("/")
def index():
    return "Welcome to my REST API!"

@app.get("/api/v1/cat")
def get_cat():
    # Use url_for to generate correct URL behind proxy
    cat_image_url = url_for('static', filename='cat.png', _external=True, _scheme='https')
    return {
        "cat_id": "1",
        "name": "Olive",
        "birthdate": "2022-03-01",
        "weight": 4.2,
        "owner": "Paul",
        "image": cat_image_url
    }

if __name__ == "__main__":
    # Bind to all interfaces; debug=False in production
    app.run(host="0.0.0.0", port=3000, debug=True)
