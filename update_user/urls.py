from django.urls import path
from update_user import views

urlpatterns = [
    path("accounts/signup", views.registration, name="registration"),
    path("accounts/signin", views.signin, name="login"),
    path("signout", views.signout, name="logout"),
    path("home",views.index,name="home"),
    path("update",views.update_details,name="update"),
    path("profile",views.list_details,name="profile")
]
