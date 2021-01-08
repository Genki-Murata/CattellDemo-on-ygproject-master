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

    # キャッテル
    path('cattell/detail/<int:page_no>/',views.cattell_detail,name='cattell_detail'),
    path('cattell/example/<int:page_no>/',views.cattell_example,name='cattell_example'),
    path('cattell/test/<int:page_no>/',views.cattell_test,name='cattell_test'),
    path('cattell/break',views.cattell_break,name='cattell_break'),
    #
]