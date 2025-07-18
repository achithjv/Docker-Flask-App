from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to Achith JV's Flask Docker App!",
        "description": "This is a containerized Flask application running inside Docker.",
        "version": "1.0.0",
        "developer": "Achith JV"
    })

@app.route('/about')
def about():
    return jsonify({
        "project": "Flask Docker Starter",
        "goal": "To demonstrate Dockerized Python Flask apps",
        "technologies": ["Python", "Flask", "Docker"]
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
