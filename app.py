from flask import Flask
from flask import request
from flask import render_template
import pymysql
import pandas as pd
import time
from matplotlib import pyplot as plot
import numpy as np
import io
import base64
#from flask.ext.images import resized_img_src
app = Flask(__name__)
#app.secret_key = 'monkey'
#images = Images(app)
@app.route('/')
def my_form():
    return render_template("index.html")
@app.route('/', methods=['GET','POST'])
def my_form_post():
    city = request.form['city']
    result= []
    baths_condition = request.form['baths_condition']
    beds_condition = request.form['beds_condition']
    area_condition = request.form['area_condition']
    baths_value = request.form['baths_value']
    beds_value = request.form['beds_value']
    area_value = request.form['area_value']
    server = pymysql.connect(host = "ec2-54-190-28-80.us-west-2.compute.amazonaws.com",user = "rem-con", passwd = "root",autocommit=True)
    cursor = server.cursor()
    sql = "USE house_list;"
    cursor.execute(sql)
    try:
        sql = """select DISTINCT street,baths,beds,city,pincode,price from house_info where baths %s %s and beds %s %s and city = '%s' and area %s %s order by price DESC """%(baths_condition,baths_value,beds_condition, beds_value,city,area_condition,area_value)
        #return sql
        cursor.execute(sql)
        x=""
        result = (cursor.fetchall())
        y1= """ <div style="text-align: center;"> <head><style> #customers tr:nth-child(even){background-color: #f2f2f2;} \
            #customers tr:hover {background-color: #ddd;} #customers th {padding-top: 12px;\
            padding-bottom: 12px;text-align: left;background-color: #4CAF50;color: white;}\
            table, th, td {border: 1px solid black;</style></head>"""
        y = """<table id="customers"> <tr><th><center>S.No</center></th> \
            <th><center>STREET</center></th> <th><center>BATHS</center></th> \
            <th><center>BEDS</center></th> <th><center>CITY</center></th> \
            <th><center>PINCODE</center></th> <th><center>PRICE</center></th> \
            </tr>"""
        result_table=[]
        for i in range(len(result)):
        	x += "<tr> <td>"+str(i+1)+"</td> <td>"+str(result[i][0])+"</td> <td>"\
                +str(result[i][1])+"</td> <td>"+str(result[i][2])+"</td> <td>"+str(result[i][3])\
                +"</td> <td>"+str(result[i][4])+"</td> <td>$"+str(result[i][5])+"</td> </tr>"
        for i in range(len(result)):
            u = {"street": result[i][0],"city":result[i][3]}
            result_table.append(u)
        img = io.BytesIO()
        df = pd.DataFrame(result_table)
        df1 = df.groupby(['city'],as_index=False).count()
        plot.figure(figsize=(20,20))
        width = 0.6
        plot.barh(df1.city,df1.street, label ='Number of houses having Bath>='+baths_value)
        for a,b in zip(df1.street,df1.city):
        	plot.text(a,b, str(a))
        plot.xlabel('total house in that area')
        plot.ylabel('cities')
        plot.rcParams.update({'font.size': 22})
        plot.legend()
        cc= "static/"+ city+".png"
        plot.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        hs= '<img src="data:image/png;base64,{}" height="800" width="800">'.format(plot_url)
        return render_template('index.html')+(y1 + y + x+ """</table>""" )+ hs +"""</div>"""
    except:
    	return render_template('index.html') + """no results found.Please try another search criteria"""
def execute_query():
    server = pymysql.connect(host = "ec2-54-190-28-80.us-west-2.compute.amazonaws.com",user = "rem-con", passwd = "root",autocommit=True)
    cursor = server.cursor()
    sql = "USE house_list;"
    cursor.execute(sql)
    

if __name__ == '__main__':
	app.debug = True
	app.run(use_reloader=True)