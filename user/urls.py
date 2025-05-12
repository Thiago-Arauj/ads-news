from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(tamplate_name='registration/login.html', next_page='add_news')),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
