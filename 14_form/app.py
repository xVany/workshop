# Team Name: Sleepy Programmers: Andy Lin, Shadman Rakib, Raymond Yeung
# SoftDev
# K14 -- Forms using Flask
# 2021-10-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' ) # Render the login template


@app.route("/auth", methods=['GET', 'POST']) # , methods=['GET', 'POST'])
def authenticate():
    # The requests property contains the values property. The value property contains
    # data from both requests.args and requests.form. 

    username = request.values['username'] 

    # request.method specifies whether the request in our case specifies if it is a GET or POST request.
    request_method = request.method

    #response to a form submission. passes down the username and method
    return render_template('auth.html', username=username, method=request_method)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
