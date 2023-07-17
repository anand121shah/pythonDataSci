from flask import Flask, jsonify

app = Flask(__name__)

# Sample student data
student = {
    'name': 'John Doe',
    'marks': 90,
    'id': 12345
}

@app.route('/', methods=['GET'])
def get_student_details():
    return jsonify({
        'name': student['name'],
        'marks': student['marks'],
        'id': student['id']
    })

if __name__ == '__main__':
    app.run()
