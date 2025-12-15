from django.urls import path
from . import views

urlpatterns = [
    path("", views.signuppage, name='signuppage'),
    path("profile/", views.profilepage, name='profilepage'),
    path("profile/edit/", views.editprofile, name='edit-profilepage'),
    path("profile/delete/", views.deleteprofile, name='delete-profilepage'),
    path("login/", views.loginpage, name='loginpage'),
    path("logout/", views.logoutpage, name='logoutpage'),
    path("home/", views.homepage, name="homepage"),
    path("about/", views.aboutpage, name="aboutpage"),
    path("contact/", views.contactpage, name="contactpage"),
    path("form/", views.addform, name='formpage'),
    path("form/update/<int:id>", views.updatetask, name='update-task'),
    path("form/delete/<int:id>", views.deletetask, name='delete-task'),
    path("task/complete/<int:id>", views.completetask, name='complete-task'),
    path("staff/dashboard/", views.staffdashboard, name='staffdashboard'),
    path("dashboard/", views.dashboardstatus, name='dashboard-status'),

]
