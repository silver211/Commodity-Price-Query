
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import csv
URLs={'gold':"https://www.investing.com/commodities/gold-historical-data",
'silver':"https://www.investing.com/commodities/silver-historical-data"}


def get_data(metal_name):
    URL=URLs[metal_name]
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    response=requests.get(URL,headers=headers)
    if response.status_code==200:
        html=response.content
        soup=BeautifulSoup(html,'lxml')
        table=soup.find("table",{"class":"genTbl closedTbl historicalTbl"})
        col_names=table.find("thead").find_all('th',{"data-col-name":["date","price"]})
        temp_col=[]
        for name in col_names:
            temp=name.text
            temp_col.append(temp)
        data=table.find("tbody").find_all("tr")
        temp_data=[]
        for rows in data:
            td=rows.find_all("td")
            row=[td[0].text,td[1].text.replace(',','')]
            temp_data.append(row)
        df=pd.DataFrame(temp_data,columns=temp_col)
        filename='.'.join([metal_name,'csv'])
        df.to_csv(filename,index=False,header=True,quoting=csv.QUOTE_NONNUMERIC)


            
        
        

if __name__=="__main__":
    get_data('gold')
    get_data('silver')
