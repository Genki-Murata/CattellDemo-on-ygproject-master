from django.urls import path
from . import views

urlpatterns = [
    path('', views.system_terms, name='system_terms'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('top/', views.top, name='top'),
    path('test/<int:page_no>/',views.test,name='test'),
    path('test_close/',views.test_close,name='test_close'),
    path('participant_index', views.participant_index, name='participant_index'),
    path('participant_show/<int:user_id>/', views.participant_show, name='participant_show'),
]