from django.urls import path

from work_app import views, api_view

urlpatterns = [
    path("",views.home,name="home"),
    path("userlist",views.userlist,name="userlist"),







    ###  API VIEWS  ###
    path('user_registration', api_view.user_registration, name='user_registration'),
    path("Mechanic_registration",api_view.Mechanic_registration,name='Mechanic_registration'),
    path("login_views",api_view.login_views,name="login_views"),
    path('Wrequest_view',api_view.Wrequest_view, name='Wrequest_view'),
    path('workshopview', api_view.workshopview, name='workshopview'),

]
