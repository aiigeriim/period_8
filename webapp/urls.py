from django.urls import path

from webapp.views import TaskDetail, TaskCreate, TaskUpdate, TaskDelete
from webapp.views import ProjectCreate, ProjectUpdate, ProjectList, ProjectDelete, ProjectDetail, ProjectAddParticipants

app_name = "webapp"

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list'),
    path('project/add/', ProjectCreate.as_view(), name='create_project'),
    path('project/detail/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='update_project'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='delete_project'),
    path('project/<int:pk>/add_participant/', ProjectAddParticipants.as_view(), name='project_add_participants'),

    path('task/detail/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('project/<int:pk>/task/add/', TaskCreate.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name='update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='delete'),
]
