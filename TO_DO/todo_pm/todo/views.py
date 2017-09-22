from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.response import SimpleTemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
import random

from todo.models import Math

def operations(request):
    number1 = random.randint(1,30)
    number2 = random.randint(1,30)
    operatori = ['+','-','/','*']
    index_operator = random.randint(0,3)
    rezultat = 0

    if operatori[index_operator] == '+':
        rezultat = number1 + number2
    if operatori[index_operator] == '-':
        rezultat = number1 - number2
    if operatori[index_operator] == '*':
        rezultat = number1 * number2
    if operatori[index_operator] == '/':
        rezultat = number1/number2

    math_entry = Math(operand_one = number1,operand_two = number2, operation = operatori[index_operator],answer = rezultat)
    math_entry.save()

    return SimpleTemplateResponse(template='todo_list.html', context={'operand_one': number1, 'operand_two': number2,
                                                                      'operation': operatori[index_operator],
                                                                      'id_quizz': math_entry.id})
@csrf_exempt
def results(request):
    answer = int(request.POST.get('answer'))
    id_quizz = int(request.POST.get('id_quizz'))
    print(answer)
    print(id_quizz)
    quizz = get_object_or_404(Math,id=id_quizz)
    print(quizz.answer)
    if answer == quizz.answer:
        return SimpleTemplateResponse(template='results.html',context={'ecuation':quizz,'statement':"Correct!"})
    elif answer == "":
        return SimpleTemplateResponse(template="results.html",context={'statement':'You didn.t write anything!'})
    else:
        return SimpleTemplateResponse(template="results.html",context={'ecuation':quizz,'statement':'Wrong!'})
