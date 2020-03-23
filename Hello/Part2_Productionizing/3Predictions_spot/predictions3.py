import pickle
from flask import Flask, request, render_template, url_for
import numpy as np

with open('rcv_final_20190516.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict', methods=['POST'])
def predict():
    """Example endpoint returning a predicted score for new recipe
    ---
    parameters:
      - name: ingredients_weight
        type: float
        required: true
      - name: ingredients_count
        type: number
        required: true
    """
    if request.method == 'POST':
        ing_wt = request.form['weight']
        ing_count = request.form['count']

        wt = float(ing_wt)
        ct = float(ing_count)
    
        ing_weight = np.log(wt)    
        ing_count = np.log(ct)
    
        pred_score_log = model.predict(np.array([[ing_weight,ing_count]]))
        pred_score = np.exp(pred_score_log)
        score = round(pred_score[0],2)
    return render_template('result.html', prediction = score)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
