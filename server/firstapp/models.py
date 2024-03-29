from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

#If you change the models in this fileyou will need to update
#the database schema. Django will do this for you and migrate
#any data as well. You just need to run the following commands:
#  python manage.py makemigrations <app name>
#  python manage.py sqlmigrate <app name> <migration number>
#  python manage.py migrate


class ToDo(models.Model):
    # Here out ToDo object has some text, a due date, a date created
    # and a completion status
    text = models.CharField(max_length=1000)
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('date due')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text

# This form lets us create new ToDo objects in our views
class ToDoForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder':'To Do Text'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Due Date', 'id':'datepicker'}))

    class Meta:
        model = ToDo
        fields = ['text', 'due_date']
