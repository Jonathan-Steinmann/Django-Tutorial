from django.db import models
import datetime
from django.utils import timezone


class Poll(models.Model):
    
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    try:
        def __str__(self):  # Python 2: def __unicode__(self):
            return self.question
    except:
        print("Please run with Python 3 else switch str to unicode (polls.models)")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <  now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):  # Python 2: def __unicode__(self):
        return self.choice_text

