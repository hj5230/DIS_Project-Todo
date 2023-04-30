from Todo.views import view
from django.urls import path

todo_path = [
    path('notebook/main/', view.notebook_main),
    path('notebook/add/', view.notebook_add),
]

urlpatterns = todo_path