from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('editor/', views.editor, name='create'),
    path('editor/<int:notes_id>/', views.editor, name='edit'),
    path('save/', views.save, name='save_new'),
    path('save/<int:notes_id>/', views.save, name='save'),
]