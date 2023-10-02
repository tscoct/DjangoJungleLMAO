
from django.http import HttpResponse

import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
#from .models import Question



def dict_l1(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]

    template = loader.get_template("dict.html")
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
    result=read_from_file()
  #[["one","u"],["tri","m"],["3","m"]]
    context = {"list_words": result}
    
    
    return HttpResponse(template.render(context))
