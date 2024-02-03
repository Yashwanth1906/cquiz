from django import forms 
from .models import questions,details

class questionform(forms.ModelForm):
    class Meta:
        model = questions
        labels = {
            'qno':('Question NO'),
            'question':('Question'),
            'choice1':('Choice1'),
            'choice2':('Choice2'),
            'choice3':('Choice3'),
            'choice4':('Choice4'),
            'anschoiceno':('Choice no. of the answer')
        }
        fields = '__all__'
class detailsform(forms.ModelForm):
    class Meta:
        model = details
        fields = '__all__'