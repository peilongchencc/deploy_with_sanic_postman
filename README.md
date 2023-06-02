# Deploy_with_sanic_postman_tutorial
本项目采用 sanic部署+ postman 测试的方式进行教学；  
文件夹名称为使用 postman 测试时，body中的数据类型选项；  
sanic==23.3.0

## Sanic 简介：  
Sanic是一个支持 **async/await** 语法的异步无阻塞框架，Sanic的处理函数必须要使用async def语法定义，因为他们是异步函数。  
### Sanic Request对象：  
**request**包含了客户端（浏览器）发过来的HTTP请求的各类数据。request不需要显示导入，Sanic内部含有。request 包含以下属性：  

| 属性   | 使用方式        | 意义                                        |
|--------|-----------------|---------------------------------------------|
| json   | request.json | 当客户端POST来的数据是json格式时，访问json数据 |
| args   | request.args | 查询字符串变量，即URL中问号?后面的部分        |
| files  | 字典            | 拥有name、body和type的文件对象的字典           |
| form   | 字典            | 以POST方式传递的form变量                     |
| body   | 字节串          | POST的原始数据                               |  
### sanic.response子模块
用于生成HTTP响应，可以生成纯文本(Plain Text，response.text())、HTML、JSON、文件（File）、数据流（Streaming）、文件流（File Streaming）、重定向（Redirect）、生数据（Raw）。  

所有返回的响应都是一个HTTPResponse类（或StreamingHTTPRsponse类），两者都派生自BaseHTTPResponse类。
导入方式类似于：  
```python
from sanic.response import json
```
### 路由：  
路由可以直接通过 @app.route("/segment", methods=["POST"]) 的方式表示，也可通过 Blueprint (蓝图)的方式表示。

```python
from sanic import Sanic
app = Sanic("HanLP-API")
@app.route("/segment", methods=["POST"])
async def function(request):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```  
### IP访问：  
注意访问的网址写法:<br>
http://localhost:8000/   ✅✅✅<br>
http://0.0.0.0:8000 &nbsp;&nbsp;&nbsp;&nbsp; ❌❌❌ 这种是外部计算机访问的方式，自己本地需要用上面的localhost方式；  
关于公共IP的设置方式，点击这里[这里](https://github.com/peilongchencc/deploy_with_sanic_postman/blob/main/x-www-form-urlencoded/blueprint-used/%E5%88%A9%E7%94%A8%E5%85%AC%E5%85%B1IP%E8%AE%BF%E9%97%AE-%E9%99%84%E8%AE%BE%E7%BD%AE%E6%96%B9%E5%BC%8F.png)  。  
## Postman简介：（持续更新中...）  
### 为什么选择Postman?  
如今，Postman的开发者已超过1000万(来自官网)，选择使用Postman的原因如下:  
简单易用 - 要使用Postman，你只需登录自己的账户，只要在电脑上安装了Postman应用程序，就可以方便地随时随地访问文件。  
使用集合 - Postman允许用户为他们的API调用创建集合。每个集合可以创建子文件夹和多个请求。这有助于组织测试结构。  
多人协作 - 可以导入或导出集合和环境，从而方便共享文件。直接使用链接还可以用于共享集合。  
创建环境 - 创建多个环境有助于减少测试重复(DEV/QA/STG/UAT/PROD)，因为可以为不同的环境使用相同的集合。这是参数化发生的地方，将在后续介绍。  
创建测试 - 测试检查点(如验证HTTP响应状态是否成功)可以添加到每个API调用中，这有助于确保测试覆盖率。  
自动化测试 - 通过使用集合Runner或Newman，可以在多个迭代中运行测试，节省了重复测试的时间。  
调试 - Postman控制台有助于检查已检索到的数据，从而易于调试测试。  
持续集成——通过其支持持续集成的能力，可以维护开发实践。  
### 安装：  
根据自己电脑的版本选择合适的型号安装即可，我的电脑是mac，所以安装的mac版本，然后进入workspace即可；  
### 主界面用法介绍：  
![postman主界面](https://github.com/peilongchencc/deploy_with_sanic_postman/blob/main/postman%E4%B8%BB%E7%95%8C%E9%9D%A2%E6%A0%87%E8%AF%86.png)。
### 具体用法：  
具体用法可参考我每个文件夹下的图示。  
