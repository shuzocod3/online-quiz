from django.urls import path
from quiz import views

urlpatterns = [
    path("", views.QuizListView.as_view(), name = "quiz-list"),
    path("detail/<int:pk>", views.QuizDetailView.as_view(), name = "quiz-detail"),
    path("create/", views.QuizCreateView.as_view(), name = "quiz-create"),
    path("question/<int:question_id>", views.QuestionDetailView.as_view(), name = "quiz-question"),
    path("delete/<int:pk>", views.QuizDeleteView.as_view(), name = "quiz-delete"),
    path("edit/<int:pk>", views.QuizEditView.as_view(), name = "quiz-edit"),
    path("statisticts/<str:gamecode>", views.UserAnswerListView.as_view(), name = "quiz-statistics"),
    path("create_question/", views.QuestionCreateView.as_view(), name = "question-create"),
]