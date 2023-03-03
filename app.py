from flask import Flask, render_template, jsonify
from database import load_job_from_db


app = Flask(__name__)



@app.route("/")
def hello_Koffi():
    jobs = load_job_from_db
    return render_template('home.html', 
                            jobs=jobs,
                             company_name='Koffi')

#Return json
@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == '__name__':
    app.run(host='0.0.0.0', debug=True)