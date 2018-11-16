from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    if "States" in request.args :
        state = request.args["States"]
        return render_template('2.html',state = get_state_options(), random = get_random(state))
    else:
        return render_template('2.html',state = get_state_options())

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    list=[]
    for county in counties:
        if not(county["State"] in list):
            list.append(county["State"])
    a=""
    option=""
    for state in list:
        option = option + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return option
    
def get_random(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    sum =0
    for county in counties :
        if county["State"] == state:
            sum += county["Housing"]["Housing Units"]
    return ( state + " has " + str(sum) + " houses")

if __name__=="__main__":
    app.run(debug=True, port=54321)
