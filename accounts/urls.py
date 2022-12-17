

# Django
from django.urls import path


# Views
from .views import Register,Login


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
]
