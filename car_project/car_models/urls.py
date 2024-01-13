from . import views
from django.urls import path

urlpatterns = [
    path('',views.loginview,name='login'),
    path('car',views.table_view,name='car'),
    path('logout',views.logout_view,name='LogOut'),
    path('update',views.Update_view,name='update'),
    path('delete/<int:pk>',views.Delete_view,name='delete'),

]
