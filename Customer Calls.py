#read data from the file
import pandas as pd
df=pd.read_excel("C:\\Users\\Mahmoud Hany\\Downloads\\New folder\\Customer Call List.xlsx")
df


CustomerID	First_Name	Last_Name	Phone_Number	Address	Paying Customer	Do_Not_Contact	Not_Useful_Column
0	1001	Frodo	Baggins	123-545-5421	123 Shire Lane, Shire	Yes	No	True
1	1002	Abed	Nadir	123/643/9775	93 West Main Street	No	Yes	False
2	1003	Walter	/White	7066950392	298 Drugs Driveway	N	NaN	True
3	1004	Dwight	Schrute	123-543-2345	980 Paper Avenue, Pennsylvania, 18503	Yes	Y	True
4	1005	Jon	Snow	876|678|3469	123 Dragons Road	Y	No	True
5	1006	Ron	Swanson	304-762-2467	768 City Parkway	Yes	Yes	True
6	1007	Jeff	Winger	NaN	1209 South Street	No	No	False
7	1008	Sherlock	Holmes	876|678|3469	98 Clue Drive	N	No	False
8	1009	Gandalf	NaN	N/a	123 Middle Earth	Yes	NaN	False
9	1010	Peter	Parker	123-545-5421	25th Main Street, New York	Yes	No	True
10	1011	Samwise	Gamgee	NaN	612 Shire Lane, Shire	Yes	No	True
11	1012	Harry	...Potter	7066950392	2394 Hogwarts Avenue	Y	NaN	True
12	1013	Don	Draper	123-543-2345	2039 Main Street	Yes	N	False
13	1014	Leslie	Knope	876|678|3469	343 City Parkway	Yes	No	False
14	1015	Toby	Flenderson_	304-762-2467	214 HR Avenue	N	No	False
15	1016	Ron	Weasley	123-545-5421	2395 Hogwarts Avenue	No	N	False
16	1017	Michael	Scott	123/643/9775	121 Paper Avenue, Pennsylvania	Yes	No	False
17	1018	Clark	Kent	7066950392	3498 Super Lane	Y	NaN	True
18	1019	Creed	Braton	N/a	N/a	N/a	Yes	True
19	1020	Anakin	Skywalker	876|678|3469	910 Tatooine Road, Tatooine	Yes	N	True
20	1020	Anakin	Skywalker	876|678|3469	910 Tatooine Road, Tatooine	Yes	N	True


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

customer_id	first_name	last_name	phone_number	address	paying_customer	do_not_contact	street_adress	state	zip_code
0	1001	Frodo	Baggins	123-545-5421	123 Shire Lane, Shire	Y	N	123 Shire Lane	Shire	
1	1005	Jon	Snow	876-678-3469	123 Dragons Road	Y	N	123 Dragons Road		
2	1008	Sherlock	Holmes	876-678-3469	98 Clue Drive	N	N	98 Clue Drive		
3	1010	Peter	Parker	123-545-5421	25th Main Street, New York	Y	N	25th Main Street	New York	
4	1013	Don	Draper	123-543-2345	2039 Main Street	Y	N	2039 Main Street		
5	1014	Leslie	Knope	876-678-3469	343 City Parkway	Y	N	343 City Parkway		
6	1015	Toby	Flenderson	304-762-2467	214 HR Avenue	N	N	214 HR Avenue		
7	1016	Ron	Weasley	123-545-5421	2395 Hogwarts Avenue	N	N	2395 Hogwarts Avenue		
8	1017	Michael	Scott	123-643-9775	121 Paper Avenue, Pennsylvania	Y	N	121 Paper Avenue	Pennsylvania	
9	1020	Anakin	Skywalker	876-678-3469	910 Tatooine Road, Tatooine	Y	N	910 Tatooine Road	Tatooine	
