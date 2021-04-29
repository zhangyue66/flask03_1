from flask import Flask, render_template, request, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []
@app.route("/",endpoint="index")
def index():
    return render_template("index.html")

@app.route("/add/<int:n1>/<int:n2>")
def add(n1,n2):
    if n1 > n2 and n2 > 0:
        r = n1+n2
    else:
        r = "not found!"
    return "result is " + str(r)


@app.route("/register",methods=["get","post"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        if password == repassword:
            user = {"username":username,"password":password}
            users.append(user)
        else:
            return "pass and repass not same"
        return redirect(url_for("index")) #注意这里并不是函数名字 而是上面路由endpoint的值 endpoint="index" 也可以是 “yuezhang”
    s = render_template("register.html")
    return s


@app.route("/register1",methods=["post","get"])
def register1():
    return "Registreation Successful!"


@app.route("/show")
def show():
    s = "123"
    for user in users:
        s += user["username"]

    return s

@app.route("/test")
def test():
    url = url_for("index") #映射 反向解析
    print(url)
    return "test_URL_FOR"


if __name__ == "__main__":
    app.run()