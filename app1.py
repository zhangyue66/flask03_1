from flask import Flask,request,render_template
import settings

app = Flask(__name__)
app.config.from_object("settings")

class Girl:
    def __init__(self,name):
        self.name = name
        self.gender = "female"

    def __str__(self):
        return self.name

@app.route("/show")
def show():
    name = "yuezhang"
    age = 32
    friends = ["lingzi","liuting","yingqi"]
    dict1 = {"cup":"G cup","cup1":"F Cup","cup2":"J Cup"}
    girl = Girl("fangfang")
    return render_template("show.html",name=name,age = age,gender = "male",friends = friends,dict1=dict1,girl_friend= girl)


if __name__ == "__main__":
    app.run()