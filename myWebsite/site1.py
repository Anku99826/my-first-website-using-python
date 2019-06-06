# first install flask manualy using cmd syntax: pip install flask
# first install virtaul environment manualy using cmd syntax: pip install virtualenv

from flask import Flask, render_template    #F in flask in CAPITAL
#render_template method of flask library access an html file and displays the content of the html file

app = Flask(__name__)   # saves flask object instances of flask application

#a folder named "template" should be made in the directory where the main python program file is saved
#this folder "template" contains all the html files or pages required by the render_template method in program

@app.route('/') #decorateor, view home page
def home():
    return render_template("home.html")

@app.route('/about/') #decorateor, view home page
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
