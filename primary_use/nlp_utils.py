# nlp_utils.py
import jieba
import jieba.analyse

class Fenci:
    @staticmethod
    def fenci(text):
        """分词"""
        seg_list = list(jieba.cut(text)) # "黄金板块应该在什么时期关注？"
                                         # jieba.cut(text)无法直接用，生成的是<class 'generator'>，需要用
                                         # print("/ ".join(seg_list))的形式转化。
                                         # 黄金/ 板块/ 应该/ 在/ 什么/ 时期/ 关注/ ？
        return seg_list

    @staticmethod
    def tfidf_extract_keywords(text, count=5):
        """tfidf提取关键词"""
        keywords = jieba.analyse.extract_tags(text, topK=5)
        return keywords

    @staticmethod
    def textrank_extract_summary(text, count=3):
        """textrank提取关键词"""
        keywords = jieba.analyse.textrank(text, topK=5)
        return keywords
