import datetime
import requests
import string
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import winsound


'''
url="https://www.equitymaster.com/stock-markets/8/-220/50/bse-above-rs-20-gainers-over-1-year"
page=requests.get(url).text
doc=lh.fromstring(page)
#print(doc)
soup = BeautifulSoup(page,'lxml')
#print(soup.prettify())
thead=soup.find_all('thead')
tbody=soup.find_all('tbody')
#print(t)

'''


def write_data_head_f1(thead):
    write_data=[]
    if (len(thead)!=0):
        for row in thead[0].find_all('tr'):
            cells=row.find_all('th')
            if len(cells)==6:
                write_data.append(str((cells[0].find(text=True))))
                write_data.append(str((cells[1].find(text=True))))
                write_data.append(str((cells[2].find(text=True))))
                write_data.append(str((cells[3].find(text=True))))
                #write_data.append(str((cells[4].find(text=True))))
                write_data.append(str('52-WEEK High (Rs.)'))
                write_data.append(str('52-WEEK Low (Rs.)'))
                #write_data=write_data+"\n"

    return (write_data)




def write_data_body_f1(tbody):
    write_data=[]
    i=0
    if(len(tbody)!=5):
        for row in tbody[5].find_all('tr'):
            cells=row.find_all('td')
            #write_data.append([])
            #print(len(cells))
            #input()
            if len(cells)==6:
                #print(cells)
                #input()
                write_data.append([])



                cell=cells[0].get_text()
                #cell=cell.replace(" ","")            
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                
                cell=cells[1].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)

                cell=cells[2].get_text()
                cell=cell.replace(" ","")            
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                
                cell=cells[3].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                
                #cell=cells[4].find(text=True)
                cell=cells[4].get_text()
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                cell_4=cell.split('\xa0/')
                write_data[i].append(str(cell_4[0]))
                write_data[i].append(str(cell_4[1]))
                #write_data[i].append(cell)
                '''
                cell=cells[5].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                cell_4=cell.split('\xa0/\xa0')
                write_data[i].append(str(cell_4[0]))
                write_data[i].append(str(cell_4[1]))
                #write_data[i].append(cell)
                '''


                #print(write_data)
                #input()
                
                #write_data[i].append(str(((cells[2].get_text()).replace(" ",""))))
                #write_data[i].append(str(((cells[3].find(text=True)).replace(" ",""))))
                #write_data[i].append(str(((cells[4].find(text=True)).replace(" ",""))))
                #write_data[i].append(str(((cells[5].find(text=True)).replace(" ",""))))
                #write_data[i].append(str(((cells[6].find(text=True)).replace(" ",""))))
                #cell4=str(cells[4].find(text=True))
                #cell4=cell4[30:]
                #cell4=cell4[:-26]
                #cell_4=cell4.split('\xa0/\xa0')
                #write_data[i].append(str(cell_4[0]))
                #write_data[i].append(str(cell_4[1]))
                
                i+=1
                #print(len(write_data[i-1]),i-1)
                
                
                """
                write_data=write_data+str((cells[0].find(text=True)))+"\t "
                write_data=write_data+str((cells[1].find(text=True)))+"\t"
                write_data=write_data+str((cells[2].find(text=True)))+"\t"
                write_data=write_data+str((cells[3].find(text=True)))+"\t"
                cell4=str(cells[4].find(text=True))
                cell4=cell4[30:]
                cell4=cell4[:-26]
                write_data=write_data+cell4+"\t"
                write_data=write_data+"\n"
                """
    #print(write_data)
    return(write_data)            



def write_data_text_f1(thead1,tbody1):
    write_data="\n"
    #print(type(thead1[0]))
    write_data=write_data+('='.ljust(185,"="))+"\n"
    if (len(thead1)!=0):
        write_data=write_data+(thead1[0].ljust(50," "))+' | '+thead1[1].ljust(30," ")+" | "+thead1[2].ljust(30," ")+" | "+thead1[3].ljust(11," ")+" | "+thead1[4].ljust(20," ")+" | "+thead1[5].ljust(20," ")+" | "+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
    write_data=write_data+('='.ljust(185,"="))+"\n"
    if(len(tbody1)!=0):
        for i in range(len(tbody1)):
            write_data=write_data+tbody1[i][0].ljust(50," ")+" | "
                
            for j in range(1,len(tbody1[i])):
                #write_data=write_data+tbody1[1].ljust(50,"0")
                write_data=write_data+(tbody1[i][j].replace(",","")).rjust(11," ")+" | "
                #write_data=write_data+tbody1[j].ljust(11,"0")
                #write_data=write_data+tbody1[j].ljust(11,"0")
            write_data=write_data+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
    write_data=write_data+('='.ljust(185,"="))+"\n\n\n"
    return(write_data)
    #input()



'''
def str_fixed_length(data,length):
    data=data.ljust(length," ")
    return(data)   

'''


def url_data_f1(thead,tbody):
    thead1=(write_data_head_f1(thead))
    #print(write_data)
    tbody1=(write_data_body_f1(tbody))
    #print("printing write data \n",write_data)
    return(write_data_text_f1(thead1,tbody1))
    #input()
    #print(str_fixed_length('suraj klumar',100))
    #print(tbody)


def url_beautify_f1(url):
    
    page=requests.get(url).text
    doc=lh.fromstring(page)
    #print(doc)
    soup = BeautifulSoup(page,'lxml')
    #print(soup.prettify())
    thead=soup.find_all('thead')
    tbody=soup.find_all('tbody')
    #print(t)
    return(url_data_f1(thead,tbody))

url_1="https://www.equitymaster.com/stock-markets/8/-220/50/bse-above-rs-20-gainers-over-1-year"
#print(url_beautify_f1(url_1))







################################################################








def write_data_head_f2(thead):
    write_data=[]
    #print(thead)
    #print("len  thead 0:  ",len(thead))
    #input("thead input")
    if (len(thead)!=0):
        for row in thead[0].find_all('tr'):
            cells=row.find_all('th')
            #print(len(cells))
            if len(cells)==7:
                write_data.append(str((cells[0].find(text=True))))
                write_data.append(str((cells[1].find(text=True))))
                write_data.append(str((cells[2].find(text=True))))
                write_data.append(str((cells[3].find(text=True))))
                #write_data.append(str((cells[4].find(text=True))))
                #write_data.append(str((cells[5].find(text=True))))
                #write_data.append(str((cells[6].find(text=True))))
                write_data.append(str('DAY\'S High (Rs)'))
                write_data.append(str('DAY\'S Low (Rs)'))
                write_data.append(str('52-WEEK High (Rs.)'))
                write_data.append(str('52-WEEK Low (Rs.)'))
                #write_data=write_data+"\n"
        return (write_data)

    else:
        return ()


def write_data_body_f2(tbody):
    write_data=[]
    i=0
    #print("length of tbody ",len(tbody))
    #print(tbody[5])
    #input()
    if (len(tbody)!=5):
        
        for row in tbody[5].find_all('tr'):
            cells=row.find_all('td')
            #write_data.append([])
            #print(len(cells))
            #input()
            if len(cells)==7:
                #print(cells)
                #input()
                write_data.append([])



                cell=cells[0].get_text()
                #cell=cell.replace(" ","")            
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                #print(write_data[i])
                
                cell=cells[1].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                #print(write_data[i])

                cell=cells[2].get_text()
                cell=cell.replace(" ","")            
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                #print(write_data[i])
                
                cell=cells[3].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                #print(write_data[i])
                
                #cell=cells[4].find(text=True)
                cell=cells[4].get_text()
                #print(cell)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                #print(cell)
                cell_4=cell.split('\xa0/')
                #print(cell_4)
                write_data[i].append(str(cell_4[0]))
                write_data[i].append(str(cell_4[1]))
                #write_data[i].append(cell)
                #print(write_data[i])

                #cell=cells[5].find(text=True)
                cell=cells[5].get_text()
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                cell_4=cell.split('\xa0/')
                write_data[i].append(str(cell_4[0]))
                write_data[i].append(str(cell_4[1]))
                #write_data[i].append(cell)



                #print(write_data)
                #input()
                
                #write_data[i].append(str(((cells[2].get_text()).replace(" ",""))))
                #write_data[i].append(str(((cells[3].find(text=True)).replace(" ",""))))
                #write_data[i].append(str(((cells[4].find(text=True)).replace(" ",""))))
                #write_data[i].append(str(((cells[5].find(text=True)).replace(" ",""))))
                #write_data[i].append(str(((cells[6].find(text=True)).replace(" ",""))))
                #cell4=str(cells[4].find(text=True))
                #cell4=cell4[30:]
                #cell4=cell4[:-26]
                #cell_4=cell4.split('\xa0/\xa0')
                #write_data[i].append(str(cell_4[0]))
                #write_data[i].append(str(cell_4[1]))
                i+=1
                
                #print(len(write_data[i-1]),i-1)
                
                
                """
                write_data=write_data+str((cells[0].find(text=True)))+"\t "
                write_data=write_data+str((cells[1].find(text=True)))+"\t"
                write_data=write_data+str((cells[2].find(text=True)))+"\t"
                write_data=write_data+str((cells[3].find(text=True)))+"\t"
                cell4=str(cells[4].find(text=True))
                cell4=cell4[30:]
                cell4=cell4[:-26]
                write_data=write_data+cell4+"\t"
                write_data=write_data+"\n"
                """
        #print(write_data)
        return(write_data)            
    else:
        return()





def write_data_text_f2(thead1,tbody1):
    write_data="\n"
    #print(type(thead1[0]))
    write_data=write_data+('='.ljust(185,"="))+"\n"
    #print("new len of thead: ", len(thead1))
    if (len(thead1)!=0):
        write_data=write_data+(thead1[0].ljust(50," "))+' | '+thead1[1].ljust(11," ")+" | "+thead1[2].ljust(11," ")+" | "+thead1[3].ljust(15," ")+" | "+thead1[4].ljust(16," ")+" | "+thead1[5].ljust(16," ")+" | "+thead1[6].ljust(20," ")+" | "+thead1[7].ljust(20," ")+" | "+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
        #True
    write_data=write_data+('='.ljust(185,"="))+"\n"
    #print("new len of tbody: ", len(tbody1))
    #print("outside tbody")
    if ((len(tbody1))!=0):
       for i in range(len(tbody1)):
            write_data=write_data+tbody1[i][0].ljust(50," ")+" | "
            for j in range(1,len(tbody1[i])):
                #write_data=write_data+tbody1[1].ljust(50,"0")
                write_data=write_data+(tbody1[i][j].replace(",","")).rjust(11," ")+" | "
                #write_data=write_data+tbody1[j].ljust(11,"0")
                #write_data=write_data+tbody1[j].ljust(11,"0")
            write_data=write_data+"\n"
        

        #return(write_data)
        #input()
    else:
        #print("inside else")
        write_data=write_data+"Sorry! No scrip found in this category.\n"
        #print("inside if")
    write_data=write_data+('='.ljust(185,"="))+"\n\n\n"
    return(write_data)


'''
def str_fixed_length(data,length):
    data=data.ljust(length," ")
    return(data)   

'''


def url_data_f2(thead,tbody):
    thead1=(write_data_head_f2(thead))
    #print(thead1)
    #print(write_data)
    tbody1=(write_data_body_f2(tbody))
    #print(tbody1)
    #1print("printing write data \n",write_data)
    return(write_data_text_f2(thead1,tbody1))
    #input()
    #print(str_fixed_length('suraj klumar',100))
    #print(tbody)
    #True

def url_beautify_f2(url):
    
    page=requests.get(url).text
    doc=lh.fromstring(page)
    #print(doc)
    soup = BeautifulSoup(page,'lxml')
    #print(soup.prettify())
    thead=soup.find_all('thead')
    tbody=soup.find_all('tbody')
    #print(thead)
    #print(tbody[5])
    return(url_data_f2(thead,tbody))

url_2="https://www.equitymaster.com/stock-markets/1/-220/0/bse-above-rs-20-gainers-today"
#print(url_beautify_f2(url_2))


#print(url_beautify_f1(url))



##########################################################

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
#print(gainers_losers_data)
#print("hik",len(bse_nse_data))
#print(len(bse_nse_data))
#input()
#https://www.equitymaster.com/stock-markets/6/1/0/bse-sensex-gainers-over-1-week

out_data="\n"


a=1
for i in range(1,16):
    #print("i", i)
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
        a+=1
        #print(i)

date=str((datetime.datetime.now())).split(" ")
date=date[0].replace("-","")
date='.\data\\'+date+'.txt'
#print(date)

with open(date,'w') as f:
    f.write(out_data)



winsound.Beep(720,720)
'''
for i in range(15):
    print(gainers_losers[i],end="     ")
    print(gainers_losers_data[i],end="      ")
    print("\n")
'''
