from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/Analysis")
def render_3():
    return render_template('Analysis.html')
  
@app.route("/Data")
def render_2():
    if ( "list" in request.args):
        return render_template('Data.html', list = all(request.args["list"]), mpg = carmpg(request.args["list"]) )
    else:
        return render_template('Data.html', list = all(0))
    
    
@app.route("/lowmpg")
def render_1():
    if ( "Year" in request.args):
        return render_template('Lowmpg.html', year = get_year(request.args["Year"]), lowMPG = lowestMPG(request.args["Year"]) )
    else:
        return render_template('Lowmpg.html', year = get_year(0))
    
def get_year(y):
    with open('cars.json') as cardata:
        cars = json.load(cardata)
        
    list=[]
    
    for year in cars:
        if not( year["Identification"]["Year"] in list):
            list.append(year["Identification"]["Year"])
    option=""
    for year in list:
        if(str(year) == y):
            option = option + Markup("<option value=\"" + str(year) + "\" selected>" + str(year) + "</option>")        
        else:
            option = option + Markup("<option value=\"" + str(year) + "\">" + str(year) + "</option>")
    return option
    
def lowestMPG(year):
    with open('cars.json') as cardata:
        cars = json.load(cardata)
        
    big = 100
    
    for car in cars:
         if (car["Fuel Information"]["Highway mpg"] <= big and str(car["Identification"]["Year"]) == year):
            big = car["Fuel Information"]["Highway mpg"]
        
    return big
    
def all(y):
    with open('cars.json') as cardata:
        cars = json.load(cardata)
        
    list=[] 
    option=""
    for year in cars:
        if not( year["Identification"]["ID"] in list):
            list.append( year["Identification"]["ID"])
    for year in list:        
        if(str(year) == y):
            option = option + Markup("<option value=\"" + str(year) + "\" selected>" + str(year) + "</option>")        
        else:
            option = option + Markup("<option value=\"" + str(year) + "\">" + str(year) + "</option>")
    return option

def carmpg(a):
    with open('cars.json') as cardata:
        cars = json.load(cardata)
        
    list=[] 
    
    for z in cars:
        if (str(a) == z["Identification"]["ID"] ):
            list.append( z["Fuel Information"]["Highway mpg"])
    return list
    
    
if __name__=="__main__":
    app.run(debug=True, port=54321)
