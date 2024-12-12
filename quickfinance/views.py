from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *

import random

def index(request):
    context = {'categories': Types.objects.all()}
    return render(request, 'index.html', context)

def quiz(request, id):
    try:
        quiz_type = Types.objects.get(id=id)
        context = {'skill': quiz_type.skill}
        return render(request, 'quiz.html', context)
    except Types.DoesNotExist:
        return HttpResponse("Quiz not found", status=404)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('skill'):
            question_objs = question_objs.filter(skill__skill__icontains=request.GET.get('skill'))

        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "skill": question_obj.skill.skill,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.get_answers(),
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        return JsonResponse({'status': False, 'error': str(e)}, status=500)
