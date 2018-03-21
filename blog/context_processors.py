# coding: utf8

from blog.article.models import Article

def base(request):
    types = Article.objects.get_all_article_type_and_count()
    datas = []
    for t in types:
        datas.append({'type': t[0], 'uuid': t[1], 'count': t[2]})
    result = {
        'author': 'ZiMing',
        'articlesInfo': datas
    }
    return result
