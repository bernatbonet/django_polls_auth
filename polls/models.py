from django.db import models
from django.conf import settings


class Question(models.Model):
    '''
    Question entity definition
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    ''' 
    Choice entity definition
    '''
    question = models.ForeignKey(Question, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
