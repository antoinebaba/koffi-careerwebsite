from sqlalchemy import create_engine, text

db_connection_string ="mysql+pymysql://gfbh1qbzzwlr1swclwd7:pscale_pw_oEAajXXq0ksmqwEQaxlHls2kNITK3b7PALSQqzMXMPM@ap-south.connect.psdb.cloud/kofficareers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
    "ssl":{
     "ssl_ca": "/etc/ssl/cert.pem"
    }
})

def load_job_from_db():
  with engine.connect() as conn:
     result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
     column_names = result.keys()
     jobs = []
     for row in result.all():
         jobs.append(dict(zip(column_names, row)))
     return jobs
