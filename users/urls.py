from django.urls import path
from . import views

urlpatterns = [
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
]