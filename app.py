from flask import Flask,render_template,jsonify,request
from utils import Get_Sales,load_dataset
import config

app=Flask(__name__)
@app.route('/Influencer_opt')
def Influencer_opt():
    df=load_dataset()
    return jsonify(list(df['Influencer'].unique()))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales_prediction',methods=['POST'])
def Your_product_sales_prediction():
    data=request.form
    TV=data['TV']
    Radio=data['Radio']
    Social_Media=data['Social_Media']
    Influencer=data['Influencer']

    sales=Get_Sales()
    sales_data=sales.get_sales_predictor(TV, Radio,Social_Media,Influencer)
    return jsonify({'Your_product_sales_prediction(in $)':sales_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.FLASK_PORT_NO)