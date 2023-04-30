from Todo.views import view
from django.urls import path

todo_path = [
    path('dashboard/', view.dashboard),
    path('codebook/main/', view.codebook_main),
    path('codebook/addtag/', view.codebook_addtag),
    path('codebook/deltag/<int:id>/', view.codebook_deltag)
]

urlpatterns = todo_path