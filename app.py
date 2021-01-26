from flask import *
import pickle
import sys 
from termcolor import colored, cprint 

app = Flask(__name__, static_url_path='/static')

#opening pkl file
model = pickle.load(open('blaps.v2.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('home.html')
	
@app.route("/add", methods = ['POST'])
def predict():
	if request.method == 'POST':
		#requesting input values from html form
		name = request.form['name']
		gender = int(request.form['gender'])
		married = int(request.form['married'])
		dependents = int(request.form['dependents'])
		education = int(request.form['education'])
		self_employed = int(request.form['self_employed'])
		app_income = int(request.form['app_income'])
		coapp_income = int(request.form['coapp_income'])
		loan_amount = int(request.form['loan_amount'])
		credit_history = int(request.form['credit_history'])
		
		
		#predicting variables 
		prediction = model.predict([[gender, married, dependents, education, 
                               self_employed, app_income, coapp_income, loan_amount, credit_history]])
		pred = prediction[0]
		out = "Error"
		if pred ==1:out = "Approved!!"
		else: out = "Declined!!"
			
		return render_template('home.html', results = out)

		

if __name__ == "__main__":
	app.run(debug = True)