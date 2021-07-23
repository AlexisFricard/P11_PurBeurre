from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("account", views.account, name='account'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("log_out", views.log_out, name='log_out'),
    path('legal_notices', views.legal_notices, name='legal_notices'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('modif_user', views.modif_user, name='modif_user'),
    path('pdf_view', views.pdf_view, name='pdf_view'),
]
