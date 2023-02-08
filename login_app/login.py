from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login1.html')


@app.route('/validate',methods = ["POST","GET"])
def validate():
    if request.method == 'POST' and request.form['pass'] == "abcd":

       return redirect(url_for('success'))
    #return redirect(url_for("login"))
    else:
        abort(401)

@app.route('/success')
def success():
    return "<h1> logged in successfully <h1>"    

if __name__ =='__main__':
    app.run(debug = False)