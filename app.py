from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL  

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'anu'
app.config['MYSQL_PASSWORD'] = 'anu'
app.config['MYSQL_DB'] = 'anu_cse'

mysql = MySQL(app)  

@app.route('/')
def hello_world():
    return 'hello, world'

@app.route('/getdata')
def getdata():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    results = cur.fetchall()  
    cur.close()
    return jsonify(results)

@app.route('/myname')
def anuu():
    return 'hello, world'

@app.route('/myhtml')
def myhtml():
    return render_template("home.html")

@app.route('/mydetails', methods=["GET", "POST"])
def mydetails():
   
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        address = request.form.get("address")
    else:
        name = request.args.get("name")
        city = request.args.get("city")
        address = request.args.get("address")

    return f"{name} {city} {address}"


@app.route('/register_save',methods=["GET","POST"])
def register_save():
    if request.method=="GET":
        return render_template("register.html")
    else:
        id=request.form('id')
        email=request.form.get("email")
        password=request.form.get("password")
        cur = mysql.connection.cursor()
        sql="insert into users( id,email,passwors)values(%s,%s,%s)"
        val = [id,email.password]
        cur.execute(sql,val)
        mysql.connection.commit()
        cur.close()
        return "register success"
    
if __name__ == '__main__':   
    app.run(debug=True)                   
