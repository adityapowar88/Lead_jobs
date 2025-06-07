from django.urls import path
from . import views

urlpatterns = [
    path("stepstone", views.save_stepstone_jobs, name="save_stepstone_jobs"),
    path("xing", views.save_xing_jobs, name="save_xing_jobs"),
]
