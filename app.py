from flask import Flask, render_template, request
import requests
import pickle


app = Flask(__name__, static_folder='static')
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
       # vendor = float(request.form['vendor'])
        myct=float(request.form['myct'])
        mmin=float(request.form['mmin'])
        mmax=float(request.form['mmax'])
        cach=float(request.form['cach'])
        chmin=float(request.form['chmin'])
        chmax=float(request.form['chmax'])

        prediction=model.predict([[myct, mmin, mmax, cach, chmin, chmax]])
        output = prediction[0]
        if output<0:
            return render_template('index.html',prediction_text="You are requested to change your system")
        elif (output<50 and output>0):
            return render_template('index.html',prediction_text="Better change your PC as performance is:- {}".format(output))
        elif (output<100 and output>50):
            return render_template('index.html',prediction_text="In good condition as performance is:- {}".format(output))
        elif (output<200 and output>100):
            return render_template('index.html',prediction_text="PC at it's best as performance is:- {}".format(output))
        else:
            return render_template('index.html',prediction_text='''It's strongly suggested :-"Apna laptop badalo"''')
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
