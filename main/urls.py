from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth  import views as auth_views


app_name = "main"

urlpatterns = [
    path("logout/", views.logout_request, name="logout"),
    path("", views.homepage, name="homepage"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("ticket/", views.ticket, name="ticket"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register_member/", views.register_member, name="register_member"),
    path("history/", views.history, name="history"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("lucky_number/", views.lucky_number, name="lucky_number"),
    path("affliate/", views.affliate, name="affliate"),
    path("signin/", views.signin, name="signin"),
    url(r'^lucky_number_details/(?P<ticket_id>\w+)/$', views.lucky_number_details, name='lucky_number_details'),

    path("maintenance/", views.maintenance, name="maintenance"),

    path("topup/", views.topup, name="topup"),
    path("convert/", views.convert, name="convert"),
    

]
