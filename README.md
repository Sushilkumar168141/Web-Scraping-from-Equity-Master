# Web-Scraping-from-Equity-Master
In this project, I created a python script to collect data from **870 different pages** from Equity Master (https://www.equitymaster.com/), and store it in a text file, for further analysis.

### Steps
1. Importing  libraries
```python
import datetime
import requests
import string
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import winsound
```
2. Create different url for  different pages  of the website
```python
gainers_losers=[]
for i in range(1,16):
    gainers_losers.append(str(i))
#print(gainers_losers)
bse_nse=[]
for i in range(1,16):
    bse_nse.append(str(i))
#for i in bse_nse:
#    print(i)
for i in range(21,30):
    bse_nse.append(str(i))
bse_nse.extend(['32','33','-201','-202','-203','-204','-205','-220','-301','-302','-320','air','aluminium','auto','autoc','bank','cement','chemicals','construction','energy','engg','fertilizer','consprds','food','finance','media','paint','pharma','reat','ship','sooftware','steel','telecom','textiles'])
#print(bse_nse)
#print(len(bse_nse))

gainers_losers_data=['-gainers-today','-losers-today','-up-circuit-breakers','-down-circuit-breakers','-most-active-stocks','-gainers-over-1-week','-gainers-over-1-month','-gainers-over-1-year','-losers-over-1-week','-losers-over-1-month','-losers-over-1-year','-gainers-over-3-years','-gainers-over-5-years','-losers-over-3-years','-losers-over-5-years']
bse_nse_data=['-bse-sensex','-bse-100','-bse-auto','-bse-bankex','-bse-capital-goods','-bse-consumer-durables','-bse-fmcg','-bse-healthcare','-bse-it','-bse-metal','-bse-oil-and-gas','-bse-psu','-bse-teck','-nse-50','-nse-it','-bse-a-group','-bse-b-group','-nifty-mid-cap-50','-bse-realty','-bse-power','-jr-nifty','-bank-nifty','-bse-500','-bse-200','-bse-mid-cap','-bse-small-cap','bse-rs-0-to-1','bse-rs-1-to-2','bse-rs-2-to-4','bse-rs-4-to-10','bse-rs-10-to-20','bse-above-rs-20','nse-rs-0-to-10','nse-rs-10-to-20','nse-above-rs-20','-sec-air','-sec-aluminium','-sec-auto','-sec-autoc','-sec-bank','-sec-cement','-sec-chemicals','-sec-construction','-sec-energy','-sec-engg','-sec-fertilizer','-sec-consprds','-sec-food','-sec-finance','-sec-media','-sec-paint','-sec-pharma','-sec-reat','-sec-ship','-sec-sooftware','-sec-steel','-sec-telecom','-sec-textiles']
```
3. Iterating on  each  url one by one, and collecting data from table
```python
for i in range(1,16):
    for j in range(1,59):
        url='https://www.equitymaster.com/stock-markets/'+str(gainers_losers[i-1])+'/'+str(bse_nse[j-1])+'/0/-'+bse_nse_data[j-1]+gainers_losers_data[i-1]
        out_data=out_data+gainers_losers_data[i-1]+' | '+bse_nse_data[j-1]+'\n'+str(gainers_losers[i-1])+' | '+str(bse_nse[j-1])+'\n'
        out_data=out_data+url+"\n"
        #print(url)
        
        if i in range(5):
            #pass
            out_data=out_data+url_beautify_f2(url)
            #print(url_beautify_f2(url))
        else:
            #pass
            out_data=out_data+url_beautify_f1(url)
            #print(url_beautify_f1(url))
        if (a%5==0):
            print("no. of websites : ",a)
```
4. Saving the data collected in a text file for particular date.
```python
date=str((datetime.datetime.now())).split(" ")
date=date[0].replace("-","")
date='.\data\\'+date+'.txt'
#print(date)

with open(date,'w') as f:
    f.write(out_data)

winsound.Beep(720,720)
```
5. Output <br>
![image](https://user-images.githubusercontent.com/41999180/124986166-f493c180-e058-11eb-88ba-3164950e68b4.png)

##### Output is stored  in text file uploaded in this repository.
