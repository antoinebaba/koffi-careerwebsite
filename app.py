from flask import Flask, render_template
app = Flask(__name__)

JOBS=[
    {
    'id':1,
    'title':'Engineer',
    'location':'Doha',
    'salary':'10000 Qar'
    },

     {
    'id':2,
    'title':'Supervisor',
    'location':'Ras Laffan',
    'salary':'8000 Qar'
    },

     {
    'id':3,
    'title':'Foreman',
    'location':'Dhukan',
    'salary':'6000 Qar'
    },

     {
    'id':1,
    'title':'Labor',
    'location':'Lusail',
    'salary':'4000 Qar'
    },
]

@app.route("/")
def hello_Koffi():
    return render_template('home.html', jobs=JOBS,
                           company_name='Koffi')

if __name__ == '__name__':
    app.run(host='0.0.0.0', debug=True)