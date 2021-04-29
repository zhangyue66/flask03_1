1.路由
@app.route("")
def test():
    add_url_route()
    pass

变量规则：
默认是str,int,float,path,UUID
import uuid
uuid = uuid.uuid4()

2.视图函数
返回值 字符串，dict，tuple，response，WSGI
对象 -> response响应对象
response("done",header={key:vale})

resp = make_response("done")

response.headers["aa"] = "bbb"

request对象

from flask import request

request.path
request.full_path
*****
request.args  -> get请求   http://127.0.0.1/regiester?username=yeuzhang&password=123
request.form -> Post请求

response响应：
1.str
2.dict
3.response对象
4.make_response（）
5.redirect()
6.render_template()

模板：
模板的语法:
1.在模板中获取view传递的变量值 {{ variable }}
render_template("index.html",variable = 12)

def show():
    name = "yuezhang"
    age = 32
    friends = ["lingzi","liuting","yingqi"]
    dict1 = {"cup":"G cup","cup1":"F Cup","cup2":"J Cup"}
    girl = Girl("fangfang")
    return render_template("show.html",name=name,age = age,gender = "male",friends = friends,dict1=dict1,girl_friend= girl)

{{ list.0 }} {{list[1:2] }}
{{ dict.get(key) }} {{ dict.gift1 }}
{{ instance.name }} {{ instance.attribute }} {{ instance.method }}

2.控制