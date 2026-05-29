from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('services/', views.service_list, name='service_list'),

    path('services/<int:id>/', views.service_detail, name='service_detail'),

    path('rendezvous/', views.rdv_list, name='rdv_list'),

    path('rendezvous/create/', views.rdv_create, name='rdv_create'),

    path('rendezvous/update/<int:id>/', views.rdv_update, name='rdv_update'),

    path('rendezvous/delete/<int:id>/', views.rdv_delete, name='rdv_delete'),

    path('register/', views.register, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
]

