from Todo.views import view
from django.urls import path

todo_path = [
    path('dashboard/', view.dashboard),
    # path('login/', view.login),
    # path('logout/', view.logout),
    path('codebook/main/', view.codebook_main),
    path('codebook/addtag/', view.codebook_addtag),
    path('codebook/deltag/<int:id>/', view.codebook_deltag),
    path('memorandum/main/', view.memorandum_main),
    path('memorandum/closer/<int:id>/', view.memorandum_closer),
    path('memorandum/delmemo/<int:id>/', view.memorandum_delmemo),
    path('memorandum/done/<int:id>/', view.memorandum_done),
    path('notebook/main/', view.notebook_main),
    path('notebook/add/', view.notebook_add),
]

urlpatterns = todo_path