from flask import Flask, render_template,request
import model
#flask
app = Flask(__name__)

#route
@app.route("/")
def hello():
    resml = model.ml()
    return render_template("index.html",pre = resml)
#
# @app.route("/sub",methods = ['POST'])
# def submit():
#     # HTML -> .py
#     if request.method == 'POST':
#         name = request.form["un"]
#     # .py -> HTML
#     return render_template("sub.html", testname = name)

if __name__ == "__main__":
    app.run(debug=True)