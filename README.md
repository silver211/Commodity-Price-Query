# Commodity-Price-Query
It's an API web-service to query commodity prices.

-------------------
Language Utlized: Python   
Package Utilized: beautifulsoup4, flask, pandas

---------------------
Part1: Data Fetch  
fetch_data.py will fetch the historical prices and dates of gold and silver from www.investing.com. It will create two csv file to store data locally.

Part2: Price Query  
query.py will start an API web-service on port 8080 to return saved data. To get data, you need to provide start date, end date and commodity type.  
For example, you may call it in this way:  
curl 'http://127.0.0.1:8080/commodity?start_date=2019-05-10&end_date=2019-05-22&commodity_type=silver'  
And it would return silver prices within time perion between 2019-05-10 and 2019-05-22, as well as mean and varirance.
