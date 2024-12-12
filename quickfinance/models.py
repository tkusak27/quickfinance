from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    class Meta:
        abstract = True


class Types(BaseModel):
    skill = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.skill
    

class Question(BaseModel):
    skill = models.ForeignKey(Types,on_delete= models.CASCADE)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(default = 5)
    
    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs =  list(Answer.objects.filter(question= self))
        data = []
        
        for  answer_obj in answer_objs:
            data.append({
                'answer' :answer_obj.answer, 
                'is_correct' : answer_obj.is_correct
            })
        return data
    
class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer',  on_delete =models.CASCADE)
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.answer 