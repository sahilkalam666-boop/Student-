from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = []

@app.route("/")
def home():
    return jsonify({"status": "ok"})

@app.route("/add", methods=["POST", "OPTIONS"])
def add_student():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data received"}), 400

    students.append(data)
    return jsonify({
        "message": "Student added successfully",
        "students": students
    })

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

app.run(host="0.0.0.0", port=3000)