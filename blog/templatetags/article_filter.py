from django import template

register = template.Library()


@register.filter()
def index_context(value):
    start = value.find('</', 100)
    end = value.find('>', start)
    end = 200 if end == -1 else end
    res_context = value[:end+1] + "<br/>   <a class='article-btn'>Read More</a> "
    return res_context
