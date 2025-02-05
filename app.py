from flask import Flask, render_template, request
import numpy as np
import pickle


model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def form():
        return render_template('index.html')
     

@app.route('/predict', methods=['POST'])
def predict():     
        gender = int(request.form.get('gender'))
        age = int(request.form.get('age'))
        ap = int(request.form.get('ap'))
        cgpa = int(request.form.get('cgpa'))
        ss = int(request.form.get('ss'))
        sd = int(request.form.get('sl'))
        dh = int(request.form.get('dh'))
        st = int(request.form.get('st'))
        sh = int(request.form.get('sh'))
        fs = int(request.form.get('fs'))
        fh = int(request.form.get('fh'))

        total = model.predict([[gender, age, ap, cgpa, ss, sd, dh, st, sh, fs, fh]])
        if (total[0]==1):
               total="You are in Depression"
        else:
               total="You are Not in Depression"       
        return render_template('predict.html',result= str(total))

if __name__ == '__main__':
    app.run(debug=True)
