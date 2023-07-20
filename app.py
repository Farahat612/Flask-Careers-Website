from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

JOBS = load_jobs_from_db()


@app.route("/")
def home_page():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs_api():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
