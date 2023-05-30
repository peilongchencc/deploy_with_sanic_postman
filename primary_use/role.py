# role.py

from sanic import Sanic
from sanic.response import json
from nlp_utils import Fenci

app = Sanic("HanLP-API")


@app.route("/segment", methods=["POST"])
async def segment(request):
    """分词API"""
    text = request.json.get("text")
    if not text:
        return json({"error": "Missing 'text' parameter"}, status=400)

    result = Fenci.fenci(text)
    return json({"分词结果为：": result})


@app.route("/keywords", methods=["POST"])
async def keywords(request):
    """tfidf提取关键词"""
    text = request.json.get("text")
    if not text:
        return json({"error": "Missing 'text' parameter"}, status=400)

    result = Fenci.tfidf_extract_keywords(text)
    return json({"使用 TF-IDF 提取关键词的结果为：": result})


@app.route("/trk", methods=["POST"])
async def text_rank_keywords(request):
    """textrank提取关键词"""
    text = request.json.get("text")
    if not text:
        return json({"error": "Missing 'text' parameter"}, status=400)

    result = Fenci.textrank_extract_summary(text)
    return json({"使用TextRank 提取关键词的结果为：": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
