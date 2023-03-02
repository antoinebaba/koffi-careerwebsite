from sqlalchemy import create_engine, text

db_connection_string ="mysql+pymysql://gfbh1qbzzwlr1swclwd7:pscale_pw_oEAajXXq0ksmqwEQaxlHls2kNITK3b7PALSQqzMXMPM@ap-south.connect.psdb.cloud/kofficareers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
    "ssl":{
     "ssl_ca": "/etc/ssl/cert.pem"
    }
})

with engine.connect() as conn:
    result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
    
    print("type(result):", type(result))
    result_all = result.all()
    print("type(result.all()):", type(result_all))
    first_result = result_all[0]

    print("type(first_result):", type(first_result))
    first_result_dict = dict(result_all[0].__dict__)
    print("type(first_result_dict):", type(first_result_dict))
    print(first_result_dict)

