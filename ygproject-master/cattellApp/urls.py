from django.urls import path
from . import views

urlpatterns = [
    path('cattell/detail/<int:page_no>/',views.cattell_detail,name='cattell_detail'),
    path('cattell/example/<int:page_no>/',views.cattell_example,name='cattell_example'),
    path('cattell/test/<int:page_no>/',views.cattell_test,name='cattell_test'),
    path('cattell/break',views.cattell_break,name='cattell_break'),
]