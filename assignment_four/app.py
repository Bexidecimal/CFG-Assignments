from flask import Flask, jsonify, request
from db_utils import get_all_monster_records, delete_monster_by_id, get_monster_record, create_monster_records

app = Flask(__name__)


# Test to see if the page was working and because I miss HTML!
@app.route("/", methods=["GET"])
def index():
    return "<h1>Hello</h1>"

# Routing to get all monsters in DB
@app.route("/monsters", methods=["GET"])
def get_all_monsters():
    return jsonify(get_all_monster_records())

# Routing to create a monster in the DB
@app.route("/monster", methods=["POST"])
def create_monster():
    return jsonify(create_monster_records(request.json))

# Routing to retrieve a singular monster by ID
@app.route("/monster/<int:id>", methods=["GET"])
def get_monster_info(id):
    return jsonify(get_monster_record(id))

# Routing to delete a monster from the DB
@app.route("/monster/<int:id>", methods=["DELETE"])
def del_monster_by_id(id):
    return jsonify(delete_monster_by_id(id))


if __name__ == "__main__":
    app.run(debug=True)