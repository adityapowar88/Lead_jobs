from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("stepstone", views.save_stepstone_jobs, name="save_stepstone_jobs"),
    path("xing", views.save_xing_jobs, name="save_xing_jobs"),
=======
    path("stepstone/", views.save_stepstone_jobs, name="save_stepstone_jobs"),
>>>>>>> ebe54271ce29f739885b798cf0087997138a7cea
]
