from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("display/", views.display, name="display"),
    path("record/", views.record, name="record"),
    path("delete_record/<int:id>/", views.delete_record, name="delete_record"),
    path("update_record/<int:id>/", views.update_record, name="update_record"),
]
