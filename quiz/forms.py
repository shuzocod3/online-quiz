from django import forms
from .models import Quiz, Questions, Answer

class QuizFormCreate(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['media', 'title', 'description']

class QuizFormEdit(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['media', 'title', 'description']


class AnswerForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Questions.objects.all(), widget=forms.HiddenInput())
    answer = forms.ModelChoiceField(queryset=Answer.objects.none(), widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['question'].initial = question
        self.fields['answer'].queryset = question.answers.all()

class QuestionFormCreate(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['media', 'quiz', 'content']