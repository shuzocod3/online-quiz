from django.shortcuts import render, get_object_or_404, redirect
from quiz import models
from django.urls import reverse_lazy
from .forms import QuizFormCreate, AnswerForm, QuizFormEdit
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView, UpdateView
from .mixins import UserIsOwnerMixin
import random
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Questions, UserAnswer


# Create your views here.


class QuizListView(ListView):
    model = models.Quiz
    context_object_name = "quiz"
    template_name = "quiz/quiz_list.html"


class QuizDetailView(DetailView):
    model = models.Quiz
    context_object_name = "quiz"
    template_name = "quiz/quiz_detail.html"


class QuizCreateView(CreateView):
    model = models.Quiz
    template_name = "quiz/quiz_create.html"
    form_class = QuizFormCreate
    success_url = reverse_lazy("quiz-list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class QuizDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Quiz
    template_name = "quiz/quiz_delete.html"
    success_url = reverse_lazy('quiz-list')


class QuizEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Quiz
    template_name = "quiz/quiz_edit.html"
    form_class = QuizFormEdit
    success_url = reverse_lazy('quiz-list')


class QuestionDetailView(FormView):
    model = models.Questions
    template_name = "quiz/question_detail.html"
    form_class = AnswerForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        question = get_object_or_404(Questions, pk = self.kwargs["question_id"])
        kwargs['question'] = question
        return kwargs

    def form_valid(self, form):
        question = form.cleaned_data['question']
        answer = form.cleaned_data['answer']
        next_question = Questions.objects.filter(quiz=question.quiz, id__gt=question.id).first()
        first_question = Questions.objects.filter(quiz=question.quiz).first().id
        if question.id == first_question:
            min_number = 1000
            max_number = 9999
            random_integer = str(random.randint(min_number, max_number))
            self.request.session["gamecode"] = random_integer
        user_answer = UserAnswer(id_answer=answer, id_user=self.request.user, id_quiz=question.quiz, gamecode=self.request.session["gamecode"])
        user_answer.save()
        if next_question:
            return redirect('quiz-question', question_id=next_question.id)
        else:
            return redirect('quiz-statistics', gamecode=self.request.session["gamecode"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = get_object_or_404(Questions, pk = self.kwargs["question_id"])
        return context

class UserAnswerListView(ListView):
    model = models.UserAnswer
    context_object_name = "useranswers"
    template_name = "quiz/quiz_statistics.html"

    def get_queryset(self):
        gamecode = self.kwargs.get("gamecode")
        return UserAnswer.objects.filter(gamecode=gamecode)