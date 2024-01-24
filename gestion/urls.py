from django.urls import path
from .views import createUser, save_users, tables, list_table, showIndex

urlpatterns = [
    path('create/', createUser),
    path('', showIndex, name='inicio'),
    path('new/', save_users),
    path('tables/', tables, name='tables'),
    path('list_empleados/', list_table, name='listar_empleados')
]