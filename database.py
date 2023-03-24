from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
    "ssl":{
     "ssl_ca": "/etc/ssl/cert.pem"
    }
})

def load_jobs_from_db():
  with engine.connect() as conn:
     result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
     column_names = result.keys()
     jobs = []
     for row in result.all():
         jobs.append(dict(zip(column_names, row)))
     return jobs

#Defined job load job
def load_job_from_db(id):
   with engine.connect() as conn:
      result = conn.execution_options(stream_results=True).execute(
         text(f"SELECT * FROM jobs WHERE id = {id}"),
      )
      rows = []
      for row in result.all():
        rows.append(row._mapping)
      if len(rows) == 0:
         return None
      else:
        return [dict(row) for row in rows]

def add_application_to_db(job_id, data):
   with engine.connect() as conn:
      query = text("INSERT INTO applications (job_id, full_name, email, linkedin, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin, :education,:work_experience, :resume_url)")
      conn.execute(query,{
                   'job_id' : job_id,
                   'full_name'  :data['full_name'],
                   'email' : data['email'],
                   'linkedin' : data['linkedin'],
                   'education' : data['education'],
                   'work_experience' : data['work_experience'],
                   'resume_url' : data['resume_url']
                   })
