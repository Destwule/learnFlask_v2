from flask import Flask, render_template, jsonify, request
from db import load_jobs_from_db, Job, load_job_from_db


app = Flask(__name__)



@app.route("/")
def hello_world():
	jobs = load_jobs_from_db()
	return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
	jobs = load_jobs_from_db()
	return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
	job = load_job_from_db(id)
	if not job:
		return '<h1>Not found</h1>'
	return render_template('jobpage.html', job=job)

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
	data = request.form
	job = load_job_from_db(id)
	return render_template("application_submited.html", application=data, job=job)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
