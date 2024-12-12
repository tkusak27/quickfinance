from django.urls import path
from quickfinance.views import index, quiz, get_quiz

urlpatterns = [
    path('', index, name='index'),
    path('quiz/<int:id>/', quiz, name='quiz'),  # Add path to handle quiz by ID
    path('api/get-quiz/', get_quiz, name='get_quiz'),
]