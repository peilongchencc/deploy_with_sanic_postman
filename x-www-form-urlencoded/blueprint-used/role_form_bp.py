from sanic import Sanic
from sanic.response import json # 这个函数用于创建一个JSON响应对象，可以将Python字典转换为JSON格式，
                                # 并将其作为响应返回给客户端(即前端界面)。
from sanic import Blueprint
from nlp_utils_form_bp import Fenci

# 创建Sanic应用程序
app = Sanic("HanLP-API")
# 创建蓝图对象
bp1 = Blueprint('blueprint1', url_prefix='/bp1')    # url_prefix 表示该蓝图的公共前缀；
bp2 = Blueprint('blueprint2', url_prefix='/bp2')
"""
蓝图可通过公共前缀对路由进行命名空间隔离，即支持下面这种写法：
@bp1.route("/segment", methods=["POST"])
@bp2.route("/segment", methods=["POST"])

不必担心url的部分重复，因为前缀不一样，所以对应的网址也不一样。
http://localhost:8000/bp1/segment
http://localhost:8000/bp2/segment
"""

# 定义路由和处理程序 - Blueprint 1
# 路由（Route）指的是将URL（Uniform Resource Locator）与相应的处理程序（Handler）或视图函数关联起来的机制。
# 区别于 x-www-form-urlencoded 中使用的 @app.route("/segment", methods=["POST"])，
# 因为蓝图会注册到应用程序(app)，所以直接用 @bp1.route("/segment", methods=["POST"]) 的方式；
@bp1.route("/segment", methods=["POST"])    
async def segment(request):
    """分词API"""
    text = request.form.get("question")
    label = request.form.get("answer")
    if not text:
        return json({"报错了": "bp1提醒您：笨蛋，你没填question的内容。"}, status=400)
    if not label:
        return json({"报错了": "bp1提醒您：笨蛋，你没填label的内容。"}, status=400)

    re_text = Fenci.fenci(text)
    re_label = Fenci.fenci(label)
    return json({"这里是bp1中question的分词结果为：": re_text,
                 "这里是bp1中answer的分词结果为：": re_label})

@bp2.route("/segment", methods=["POST"])
async def segment(request):
    """分词API"""
    text = request.form.get("question")
    label = request.form.get("answer")
    if not text:
        return json({"报错了": "bp2提醒您：笨蛋，你没填question的内容。"}, status=400)
    if not label:
        return json({"报错了": "bp2提醒您：笨蛋，你没填answer的内容。"}, status=400)

    re_text = Fenci.fenci(text)
    re_label = Fenci.fenci(label)
    return json({"这里是bp2中question的分词结果为：": re_text,
                 "这里是bp2中answer的分词结果为：": re_label})

@bp1.route("/keywords", methods=["POST"])
async def keywords(request):
    """tfidf提取关键词"""
    text = request.form.get("question")
    if not text:
        return json({"error": "Missing 'question' parameter"}, status=400)

    result = Fenci.tfidf_extract_keywords(request)
    return json({"使用 TF-IDF 提取关键词的结果为：": result})


@bp1.route("/trk", methods=["POST"])
async def text_rank_keywords(request):
    """textrank提取关键词"""
    text = request.form.get("question")
    if not text:
        return json({"error": "Missing 'question' parameter"}, status=400)

    result = Fenci.textrank_extract_summary(request)
    return json({"使用TextRank 提取关键词的结果为：": result})

# 将蓝图注册到应用程序
app.blueprint(bp1)
app.blueprint(bp2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
