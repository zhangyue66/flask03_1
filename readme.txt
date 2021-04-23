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