from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
	{
		"id": 1,
		"title": "Data Analyst",
		"location": "Abuja, Nigeria",
		"salary": "NGN. 90,000",
	},
	{
		"id": 2,
		"title": "Data Analyst",
		"location": "Lagos, Nigeria",
		"salary": "NGN. 90,000",
	},
	{
		"id": 3,
		"title": "Frontend Engineer",
		"location": "Remote",
		# "salary": "USD. 109, 000",
	},
	{
		"id": 4,
		"title": "Backend Engineer",
		"location": "San Francisco, USA",
		"salary": "USD. 120,000",
	}
]

@app.route("/")
def hello_world():
	return render_template("home.html", jobs=JOBS, company_name="Monty")

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
