from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from database import load_job_from_db


app = Flask(__name__)



@app.route("/")
def hello_Koffi():
    jobs = load_jobs_from_db()
    return render_template('home.html',
                            jobs=jobs,
                             company_name='Koffi')

#Return json
@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

#Creationg new route for job row
@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    return render_template('jobpage.html',job=job)
#jsonify(job)

if __name__ == '__name__':
    app.run(host='0.0.0.0', debug=True)