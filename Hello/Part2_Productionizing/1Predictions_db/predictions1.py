"""
Please change the below section
"""
PATH = "C:/Users/kpunyakoti/Desktop/Future/HelloFresh/"
import mysql.connector
connection = mysql.connector.connect(host = 'localhost', user='root', password='root', db= 'hellofresh')
"""
Do NOT change anything else from here
"""

import pickle
from flask import Flask, request, render_template, url_for, jsonify
import numpy as np
import pandas as pd
import json
import requests
import time
timestr = time.strftime("%Y%m%d_%H%M%S")
timestr2 = time.strftime("%H:%M:%S")

with open('rcv_final_20190516.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def get_preds():
    url = "http://localhost:5000/batch"
    #header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    print("getting new data")

    ratings = pd.read_sql_query("select recipe_code from recipe_ratings where score = 'NaN'", connection)
    ingredients = pd.read_sql_query('select recipe_code, Ingredient, Unit_weight_amount from ingredients', connection)

    ingredients['Unit_weight_amount'] = ingredients['Unit_weight_amount'].astype(float)
    ingredients.drop_duplicates(inplace=True)
    #create ing_count
    ingredient_count = pd.DataFrame(ingredients.recipe_code.value_counts())
    ingredient_count.reset_index(inplace=True)
    ingredient_count.columns = ['recipe_code', 'ing_count']
    ingredients = pd.merge(ingredients, ingredient_count, on = 'recipe_code')

    #create ing_weight
    ing_wt = pd.DataFrame(ingredients.groupby('recipe_code')['Unit_weight_amount'].sum())
    ing_wt.reset_index(inplace=True)
    ing_wt.columns = ['recipe_code', 'ing_weight']
    ingredients = pd.merge(ingredients, ing_wt, on = 'recipe_code', how='outer')
    #drop cols
    drop_cols = ['Ingredient','Unit_weight_amount']
    for x in drop_cols:
        ingredients.drop(x, axis=1, inplace=True)
    #merge tables
    df = pd.merge(ratings, ingredients, on = 'recipe_code')

    recipe_codes = df['recipe_code']
    df.drop('recipe_code', axis=1, inplace=True)
    
    data = df.to_json(orient='records')
    resp = requests.post(url, data = json.dumps(data))
    
    preds = resp.json()
    preds_list = json.loads(preds)
    preds_df = pd.DataFrame()
    preds_df['recipe_code'] = recipe_codes
    preds_df['scores'] = pd.DataFrame(preds_list)
    preds_df['scores'] = preds_df['scores'].map(lambda x: round(x,2))

    preds_df.to_csv('{}Predictions_{}.csv'.format(PATH,timestr))

    ret_str = "Predictions posted successfully. Please check the file named, Predictions_"+timestr+".csv in the path "+PATH

    return ret_str

@app.route('/batch', methods=['POST'])
def batch():
    try:
        print('i am in batch')
        test_json = request.get_json(force=True)
        test = pd.read_json(test_json, orient='records')
        test = test[['ing_weight','ing_count']]
        
        #To resolve the issue of TypeError: Cannot compare types 'ndarray(dtype=int64)' and 'str'
        test['ing_weight'] = [np.log(x) for x in list(test['ing_weight'])]
        test['ing_count'] = [np.log(x) for x in list(test['ing_count'])]


    except Exception as e:
        raise e

    if test.empty:
        return(bad_request())
    else:
        print("The model has been loaded...doing predictions now...")
        log_preds = model.predict(test)
        preds = np.exp(log_preds)
        """Add the predictions as Series to a new pandas dataframe
                                OR
           Depending on the use-case, the entire test data appended with the new files
        """
        pred_scores = list(pd.Series(preds))

        final_preds = pd.DataFrame(list(pred_scores))
        print("Predictions completed")
        """We can be as creative in sending the responses.
           But we need to send the response codes as well.
        """
        responses = jsonify(final_preds.to_json(orient="records"))
        return (responses)
    
if __name__ == '__main__':
    #app.debug=True
    app.run(port=5000)
    


