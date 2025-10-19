from flask import Flask

app = Flask(__name__, static_folder="public", static_url_path="/public")

@app.get("/")
def index():
    return "Welcome to my REST API!"

@app.get("/api/v1/cat")
def get_cat():
    return {
        "cat_id": "1",
        "name": "Olive",
        "birthdate": "2022-03-01",
        "weight": 4.2,
        "owner": "Paul",
        "image": "http://127.0.0.1:3000/public/cat.png"
        
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
