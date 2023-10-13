from django.http import HttpResponse

import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
import django.middleware.csrf as cs
#from .models import Question


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def main(request):
    html = """<html><body>
    Welcome to main pagerrr.<br>
    <a href="dicta">Практика 1: Словарь</a><br>
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

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        #return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    result = read_from_file()
    #[["one","u"],["tri","m"],["3","m"]]
    context = {"list_words": result}
    template = loader.get_template("dict.html")
    return HttpResponse(template.render(context))


def dict_l1_add(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    print("requested a page...")
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
      form = NameForm(request.POST)  
      if form.is_valid():
          
          print("gothca")
          save_words(form["word1"].value(), form["word2"].value())
        # check whether it's valid:
        #if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        #return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    result = read_from_file()
    #[["one","u"],["tri","m"],["3","m"]]
    #django.middleware.csrf.get_token()
    context = {
        "list_words": result,
        "csrf_token": cs.get_token(request),
        "form": form
    }
    template = loader.get_template("add_word.html")
    return HttpResponse(template.render(context))


def save_words(word1, word2):
    with open("file", "a") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    file = open("file", "r", encoding="utf-8").read().splitlines()
    words = []

    for line in file:
        word1, word2 = line.split("-")
        words.append([word1, word2])
    return words
