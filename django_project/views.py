from django.http import HttpResponse

import datetime
from django.http import HttpResponse
from django.template import loader

#from .models import Question


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def main(request):
    html = """<html><body>
    Welcome to main pagerrr.<br>
    <a href="dict">Практика 1: Словарь</a><br>
    <a href="2">Практика </a><br>
    <a href="3">Практика </a><br>
    <a href="4">Практика </a><br>
    </body></html>"""

    return HttpResponse(html)


def index(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("post.html")
    """context = {
        "latest_question_list": latest_question_list,
    }"""
    return HttpResponse(template.render())


def dict_l1(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("dict.html")
    """context = {
        "latest_question_list": latest_question_list,
    }"""
    return HttpResponse(template.render())