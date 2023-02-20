from django.urls import path
from .views import SignupView, LoginView, UserDetailView, UserDeactivateView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/deactivate/', UserDeactivateView.as_view(), name='user_deactivate'),
]
