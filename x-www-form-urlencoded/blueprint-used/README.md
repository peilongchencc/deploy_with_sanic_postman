# 通过Blueprint使用 form.get 方法从网页获取 key-value 数据并处理：
## 代码逻辑介绍：
使用蓝图通过**公共前缀**对路由进行命名空间隔离：  
bp1 = Blueprint('blueprint1', url_prefix='/bp1')    &nbsp;&nbsp;# url_prefix 表示该蓝图的公共前缀；<br>
bp2 = Blueprint('blueprint2', url_prefix='/bp2')  

即支持下面这种写法：  
@bp1.route("/segment", methods=["POST"])  
@bp2.route("/segment", methods=["POST"])  
  
不必担心url的部分重复，因为前缀不一样，所以对应的网址也不一样。<br>
```python
http://localhost:8000/bp1/segment
http://localhost:8000/bp2/segment  
```
**解释：**  
区别于 x-www-form-urlencoded 中使用的 @app.route("/segment", methods=["POST"])，  
因为蓝图会注册到应用程序(app)，所以直接用 @bp1.route("/segment", methods=["POST"]) 的方式；  

然后使用 request.form.get("question") 的方式，从网页端获取 key 对应的 value 值，并处理。
需要获取的变量有2个：<br>
question 和 answer  

**延伸：连接阿里云服务器配置的域名也会用到蓝图。**  
假设你在阿里云服务器开启了一个 **端口为7711** 的服务，你联系管理员帮你开通这个端口。  
然后管理员给你了一个域名   https://mynet/nlp-server   ，告诉你这个域名对应的就是7711这个端口。  
此时你就可以进行如下配置：<br> 
```python
import jieba

app = Sanic("HanLP-API")

nlpBlueprint = Blueprint('match_nlp-serveri_domain_name', url_prefix='/nlp-server') # 这里使用蓝图的作用不是为了隔离命名空间，是为了进行域名匹配，匹配到 /nlp-server。

@nlpBlueprint.route("/segment", methods=["POST"])
async def segment(request):
    """分词API"""
    text = request.form.get("question")
    if not text:
        return json({"error": "Missing 'question' parameter"}, status=400)

    re_text = jieba.lcut(text)
    return json({"分词结果为：": re_text})

# 将蓝图注册到应用程序
app.blueprint(nlpBlueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7711)
```
在 postman 测试时输入 https://ci.7min.com.cn/nlp-server/answer (不需要输入端口号)，填写字段，就可连接服务。<br>
## 各文件的作用如下：
nlp_utils_form_bp.py ：提供三个函数方法，因使用了装饰器@staticmethod，所以可以不用实例化类就直接调用；<br>
role_form_bp.py ：sanic 部署文件，创建IP连接，从 postman 获取网页数据后，使用 nlp_utils_bp.py 中的方法处理数据；  
利用公共IP访问-附设置方式.png：自己使用 postman 利用外部设备通过公共IP访问成功的图片，图片中也有公共IP的查找方式；(我的电脑是mac)
## postman 中的设置如下：
1. 点击New创建一个新的测试界面；
2. 选择 http 模式；
3. 根据 role_form_bp.py 中设置的模式选择 GET 或 POST，自己选择的 POST；
4. 填入 URl；
注意访问的网址写法:<br>
http://localhost:8000/   ✅✅✅<br>
http://0.0.0.0:8000 &nbsp;&nbsp;&nbsp;&nbsp; ❌❌❌ 这种是外部计算机访问的方式，自己本地需要用上面的localhost方式；
5. body 项选择 x-www-form-urlencoded ；
6. 在下方的框中按照键值对形式填入 "question" 和 "answer" 即可；
7. 点击 send 发送数据，等待回传结果；

## postman中body下的几个选项分别是什么？如何选择？
在Postman中，Body选项用于指定请求的消息体（payload）内容。以下是在Body选项中常见的几个选项及其含义：
1. **none:** 这表示请求不包含消息体。选择此选项时，请求通常是GET或DELETE等不需要发送数据的HTTP方法。
2. **form-Data:** 当使用该选项时，请求的消息体将被格式化为multipart/form-data格式。这通常用于上传文件或通过表单提交数据。
3. **x-www-form-urlencoded:** 选择此选项将以URL编码形式发送请求的数据。🔥🔥🔥🔥🔥🔥这种格式通常用于HTML表单提交🔥🔥🔥🔥🔥🔥。
4. **raw:** 当选择此选项时，您可以手动编辑请求的消息体内容。您可以选择不同的格式，例如文本（纯文本）、JSON（应用/JSON）、XML（application/xml）等。
5. **binary:** 选择此选项以上传二进制文件。您可以选择将文件直接从磁盘上载，或者使用代码或其他方式生成二进制数据。
6. **graphQL:** 如果您正在使用GraphQL API，则可以选择此选项，并在请求的消息体中编写GraphQL查询。
7. **file:** 这个选项允许您将文件直接作为请求的消息体。您可以选择从磁盘上载文件，或者从已发送的请求中选择文件。
选择哪个选项取决于您要发送的数据类型和请求的要求。如果您要发送表单数据，您可以选择Form-Data或x-www-form-urlencoded。如果您要发送JSON数据，可以选择Raw并将Content-Type设置为application/json。如果您要上传文件，您可以选择Form-Data或Binary，具体取决于您的需求。
