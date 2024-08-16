from django.urls import path
from . import views

urlpatterns = [
    path("summarization/", views.llm_view, name="summary"),
]
