from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:page_no>/',views.cattell_detail,name='cattell_detail'),
    path('example/<int:page_no>/',views.cattell_example,name='cattell_example'),
    path('test/<int:page_no>/',views.cattell_test,name='cattell_test'),
    path('break',views.cattell_break,name='cattell_break'),
]