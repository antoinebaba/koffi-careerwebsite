from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db
from database import load_job_from_db
from  database import add_application_to_db

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

    if not job:
        return "Not Found", 404

    return render_template('jobpage.html',
                           job=job)
#jsonify(job)

@app.route("/job/<id>/apply", methods = ['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('applicationsubmit.html',
                           application = data,
                           job = job)

if __name__ == '__name__':
    app.run(host='0.0.0.0', debug=True)