from flask import Flask,render_template,request
import keras
from keras.models import load_model
app = Flase(__name__)
model = load_model("telcom_churn.hs")
@app.route('/')
def home():
    return render_template('home.html')
@app.route("/") 
def helloworld():
    return render_template("base.html")
@app.route('/assesment")
def prediction():
    return render_template("index.html")

@app.route("/predict', methods = ['POST'])
def admin():
    a= request.form[ "gender"]
    if (a = 'f'):
        a=0
    if (a== 'm'):
        a=1
    b= request.form["srcitizen"]
    if (b == 'n'):
        b=0
    if (b == 'y'):
        b=1
    c= request.form["partner"] 
    if (c=='n'):
        c=0
    if (c == 'y'):
        c=1
    d= request.form["dependents"]
    if (d =='n'):
        d=0
    if (d =='y'):
        d=1
    e= request.form["tenure"]
    f= request.form["phservices"]
    if (f == 'n'):
        f=0
    if (f == 'y'):
        f=1
    g= request.form["multi"]
    if (g == 'n'):
    
    if (g == 'n'):
        gl.g2,3-1,0,0
    if (g == 'nps'):
        gl.g2,g3-0,1,0
    if (g == 'y'):
        g1,g2,g3=0,0,1
    h= request.form["is"] 
    if (h == 'ds1'):
        h1, h2, h3=1,0,0 
    if (h == 'fo'):
        h1, h2, h3=0,1,0
    if (h == 'n'):
        h1, h2, h3=0,0,1
    i= request.form["os"]
    if (i == 'n'):
        i1,i2,i3=1,0,0 
    if (i == 'nis'):
        i1,i2,i3=0,1,0
    if (i == 'y'):
        i1,i2,i3=0,0,1 
    j= request.form["ob"]
    if (j == 'n'):
        j1, j2, j3=1,0,0
    if (j == 'nis'):
        j1,j2, j3=0,1,0
    if (j == 'y'):
        j1, j2, j3=0,0,1
    k= request.form["dp"] 
    if (k == 'n'):
        k1,k2,k3=1,0,0
    if (k == 'nis'):
        k1,k2, k3=0,1,0
    if (k == 'y'):
        k1,k2, k3=0,0,1
    1= request.form["ts"]
    if (1='n'):
        11,12,13=1,0,0

    if (1 == 'nis'):
        11,12,13 0,1,0 
    if (1 =='y'):
        11,12,13-0,0,1
    m= request.form["stv"]
    if (m == 'n'):
    m1, m2, m3=1,0,0
    if (m == 'nis'):
        m1, m2, m3=0,1,0 
    n= request.form["smv"] 
    if (n == 'n'):
        n1,n2, n3=1,0,0 
    if (n == 'nis'):
        n1,2,3=0,1,0  
    if (n == 'y):'
        n1,2,3=0,0,1
    0= request.form["contract"]
    if (o == 'mtm'):
        01,02,03-1,0,0
    if (o == 'oyr'):   
        01,02,03-0,1,0
    if (o == 'tyrs'):
        01,02,03-0,0,1
    p= request.form["pmt"]
    if (p == 'ec'):
        p1, p2,p3,p4=1,0,0,0
    if (p == 'mail'): 
        p1, p2,p3,p4=0,1,0,0 
    if (p == 'bt'): 
        p1, p2,p3,p4=0,0,1,0
    if (p == 'cc'):
        p1, p2,p3,p4=0,0,0,1
    q= request.form["p1b"]  
    if (q == 'n'):
    q= request.form["plb"]
    if (q == 'n'):
        q=0
    if (q == 'y'):
        q=1
r= request.form["mcharges"]
s= request.form["tcharges"]

t-[[int (g1), int(g2), int (g3), int (h1), int (h2), int (h3), int(11), int(12), int(13), int(1
print(t)
x = model.predict(t)
print(x[0])
if (x[0]] <-0.5):
    y="No"
    return render_template("predno.html", z = y)

if (x[[0]] >=0.5):
    y = "Yes"
    return render_template("predyes.html", z = y)