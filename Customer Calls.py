#read data from the file
import pandas as pd
df=pd.read_excel("C:\\Users\\Mahmoud Hany\\Downloads\\New folder\\Customer Call List.xlsx")
df

#handling the duplicates values
df=df.drop_duplicates()
#drop an unseful column
df=df.drop(columns='Not_Useful_Column')
df

#cleaning the Last_Name coulmn
df['Last_Name']=df["Last_Name"].str.strip('123._/')

#cleaning the Phone_Number column
df["Phone_Number"]=df["Phone_Number"].str.replace("[^a-zA-Z0-9]","",regex=True)
df["Phone_Number"]=df["Phone_Number"].str.replace("[^a-zA-Z0-9]","",regex=True)
df["Phone_Number"]=df["Phone_Number"].str.replace("nan--","",regex=True)
df["Phone_Number"]=df["Phone_Number"].str.replace("Na--","",regex=True)

#splitting the street_adress into three columns
df[['street_adress','state','zip_code']]=df["Address"].str.split(',',n=2,expand=True)

#handling the values in the boolean columns
df['Paying Customer']=df['Paying Customer'].str.replace('Yes','Y',regex=True)
df['Paying Customer']=df['Paying Customer'].str.replace('No','N',regex=True)
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y',regex=True)
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N',regex=True)
df=df.replace('N/a','',regex=True)
df = df.fillna('')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('NNN','N',regex=True)
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('NYN','Y',regex=True)

#drop the null values in 'Do_Not_Contact' and 'Phone_Number' coulmns
for x in df.index:
    if df.loc[x,'Do_Not_Contact']=='Y':
        df.drop(x,inplace=True)
for x in df.index:
    if df.loc[x,'Phone_Number']=='':
        df.drop(x,inplace=True)
df=df.reset_index(drop=True)
#renaming the colums to the standarize names
df.columns=df.columns.str.replace('_',' ')
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df = df.rename(columns={'customerid': 'customer_id'})
df

