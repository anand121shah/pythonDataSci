from flask import Flask, jsonify

app = Flask(__name__)

# Sample student data
student = {
    'name': 'John Doe',
    'marks': 90,
    'id': 12345
}

# Route to show your name
@app.route('/students', methods=['GET'])
def show_name():
    return "Your name"

# Dynamic route to print student's name
@app.route('/students/<name>', methods=['GET'])
def get_student_name(name):
    return f"Student Name is {name}"

if __name__ == '__main__':
    app.run(port=5000)
