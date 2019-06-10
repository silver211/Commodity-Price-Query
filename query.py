from flask import Flask, jsonify,request
from datetime import datetime
import pandas as pd
app = Flask(__name__)
df_gold=pd.read_csv('gold.csv',converters={'Price':str})
df_silver=pd.read_csv('silver.csv',converters={'Price':str})
df_gold['Date']=pd.to_datetime(df_gold['Date'])
df_silver['Date']=pd.to_datetime(df_silver['Date'])
#df_gold['Price']=str(df_gold['Price'])
#df_silver['Price']=str(df_silver['Price'])
@app.route('/commodity',methods=['GET'])
def get_data():
	if 'start_date' not in request.args:
		return 'Please specify start date.\n'
	if 'end_date' not in request.args:
		return 'Please specify end date.\n'
	if 'commodity_type' not in request.args:
		return 'Please specify commodity type.\n'
	start_date=request.args['start_date']
	end_date=request.args['end_date']
	commodity_type=request.args['commodity_type']
	start_date=datetime.strptime(start_date,'%Y-%m-%d').date()
	end_date=datetime.strptime(end_date,'%Y-%m-%d').date()
	if start_date>end_date:
		return 'End date should be later than start date.'
	if commodity_type=='gold':
		df=df_gold
	elif commodity_type=='silver':
		df=df_silver
	else:
		return 'Commodity should be either gold or silver.'
	mask=(df['Date']>=start_date)&(df['Date']<=end_date)
	selected=df[mask]
	if selected.empty:
		return 'No record.\n'
	Data={}
	for index,row in selected.iterrows():
		Data.update({row['Date'].date().isoformat():float(row['Price'])})
	mean=selected['Price'].astype(float).mean()
	var=selected['Price'].astype(float).var()
	return jsonify({'data':Data,'mean':float("%.2f" % mean),'var':float("%.2f" %var)})





if __name__ == '__main__':
    app.run(debug=True,port=8080)