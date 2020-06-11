# -*- coding:utf-8 -*-
__version__ = '1.0.0.0'

import json
import math
import copy
from django import template

register = template.Library()


@register.filter(name='format_none')  # 过滤器在模板中使用时的name
def format_none(value):  # 把传递过来的参数arg替换为'~'
    if not value:
        return ''
    return value


@register.filter(name="cut")
def cut(value, arg=80):
    # text_maker = html2text.HTML2Text()
    # text_maker.ignore_links = True
    # text_maker.bypass_tables = True
    # value = text_maker.handle(value)
    value = value.replace("<br></br>", "")
    value = value.replace("&nbsp;", "")
    if len(value) > arg:
        return " %s......" % value[:arg]
    else:
        return value


@register.filter(name="strtojson")
def strtojson(str_arg):
    return json.loads(str_arg)


@register.filter(name="inttolist")
def inttolist(int_arg):
    return range(1, int_arg)


@register.filter('strftime')
def strftime(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")


@register.filter('commentcount')
def commentcount(queryset):
    return len(queryset)


@register.filter('cut_seq')
def cut_seq(value):
    count = math.ceil(len(value) / 10)
    ret = []
    ret2 = []
    for i in range(count):
        ret2.append("<span style='margin-right:10px;width:150px; display: inline-block;'>%s</span>" % value[i*10: (i+1)*10])
        if len(ret2) == 6:
            ret.append("<p style='height:20px'>%s</p>" % ("".join(copy.deepcopy(ret2))))
            ret2.clear()
    return "".join(ret)