from flask import Flask,render_template,redirect,request
import time
import pyotp
import qrcode

key="MadhuforGeeksIsBestForEverything"

totp = pyotp.TOTP(key)

app=Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/loginotp',methods=['post'])
def loginotp():
    otp=request.form['otp']
    state=totp.verify(int(otp))
    if state==True:
        return render_template('index.html',res='otp valid')
    else:
        return render_template('index.html',err='Invalid Otp')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)