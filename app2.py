from flask import Flask,request,render_template
import settings

app = Flask(__name__)
app.config.from_object("settings")

@app.route("/show1")
def show1():
    girls = ["Yang Mi","Ru Hua","Tong Li Ya","Feng Jie","Gao Lingzi","Cheng Xiao"]
    cups = ["G","A","A","B","H","G"]
    users = [
        {"user":"1","password":"123","address":"SZ","phone":1392345},
        {"user":"2","password":"123332","address":"GZ","phone":13923421235},
        {"user":"3","password":"12322","address":"BJ","phone":1392312345},
        {"user":"4","password":"123111","address":"SH","phone":1392312345},
        {"user":"5","password":"123444","address":"CD","phone":139266345}
    ]
    return render_template("show_1.html",girls = girls,users = users)


if __name__ == "__main__":
    app.run()