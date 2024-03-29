from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    return HttpResponse("hello world,You're at the polls index.")
def detail(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return  render(request,'polls/detail.html',{'question':question})
# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request,'polls/detail.html',{'question':question})
        #return HttpResponse("You're looking ai the question %s."%question_id)
def result(request,question_id):
    response= "You're looking at the result of question %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You're looking at the result of question %s."%question_id)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list':latest_question_list,
#     }
#     return HttpResponse(template.render(context,request))
    # Leave the rest of the views (detail, results, vote) unchanged
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return  render(request,'polls/index.html',context)