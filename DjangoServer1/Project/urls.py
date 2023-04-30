from Todo.views import view
from django.urls import path

todo_path = [
    path('memorandum/main/', view.memorandum_main),
    path('memorandum/closer/<int:id>/', view.memorandum_closer),
    path('memorandum/delmemo/<int:id>/', view.memorandum_delmemo),
    path('memorandum/done/<int:id>/', view.memorandum_done),
]

urlpatterns = todo_path