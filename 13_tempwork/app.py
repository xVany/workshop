# Temp Team - Cameron Nelson, Austin Ngan, Raymond Yeung
# SoftDev
# K13 - Reading & Parsing CSV file
# 2021-10-08

import random
from flask import Flask, render_template;
app = Flask(__name__);

@app.route("/occupy_flask_st")
def code():
    file = open("data/occupations.csv");
    lines = file.read().split("\n");
    del lines[0]; #Remove "Job Class, Percentage" line
    split = [];
    for i in lines:
        if "," in i:
            #remove quotes, split string into job and %, then convert % to float
            i = i.replace("\"","");
            comma = i.rsplit(",",2);
            print(str(comma)+ "\n");
            comma[1] = float(comma[1]);
            #add to necessary arrays
            split.append(comma);

    del split[len(split)-1]; # Remove "Total" as a job
    dictionary = {};
    for i in split:
        dictionary[i[0]] = i[1];

    weighted_choice = (random.choices(list(dictionary), weights=dictionary.values()))[0];

    return render_template('tablified.html',randjob=weighted_choice,dictionary=split);

if (__name__ == "__main__"):
    app.debug = True;
    app.run();

