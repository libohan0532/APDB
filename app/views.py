
from django.shortcuts import render
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger
from app.custom_paginator import CustomPaginator
from django.http import HttpResponse

class HomeView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):#传递可变参数
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get(self, request):
        obj_list = DataModel.objects.all()#理论上可以查询所有字段
        key = request.GET.get("key", "")
        value = request.GET.get("value", "")
        if key == 'locus' and value:
            obj_list = obj_list.filter(locus=value)
        if key == 'organism' and value:
            obj_list = obj_list.filter(organism__contains=value)
        if key == 'definition' and value:
            obj_list = obj_list.filter(definition__contains=value)
        if key == 'comment' and value:
            obj_list = obj_list.filter(comment__contains=value)
        if key == 'taxonomy' and value:
            obj_list = obj_list.filter(taxonomy__contains=value)
        current_page = request.GET.get("page", '1')
        paginator = CustomPaginator(current_page, 9, obj_list, 10)
        try:
            paginator = paginator.page(current_page)  # 获取前端传过来显示当前页的数据
        except PageNotAnInteger:
            # 如果有异常则显示第一页
            paginator = paginator.page(1)
        except EmptyPage:
            # 如果没有得到具体的分页内容的话,则显示最后一页
            paginator = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {"paginator": paginator, "key": key, "value":value})


class DetailView(View):
    def get(self, request):
        locus = request.GET.get("locus")
        obj = DataModel.objects.get(locus=locus)
        return render(request, 'detail.html', {"obj": obj})
    #将搜索获得的locus名称传给前端

class IntroView(View):
    def get(self, request):
        return render(request,'introduction.html')