from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analyst",
    'location': "Cairo, EG",
    'salary': "10K EGP"
  },
  {
    'id': 2,
    'title': "Data Scientist",
    'location': "Giza, EG",
    'salary': "15K EGP"
  },
  {
    'id': 3,
    'title': "Software Engineer",
    'location': "Cairo, EG",
    'salary': "20K EGP"
  },
  {
    'id': 4,
    'title': "Network Engineer",
    'location': "Tanta, EG",
    'salary': "12K EGP"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__" :
  app.run(host='0.0.0.0', debug=True)
  
  
