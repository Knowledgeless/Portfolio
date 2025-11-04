
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("graphics/", views.graphics, name="graphics"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),


]
