

# Django
from django.urls import path

# Views
from .views import *


urlpatterns = [
    path('random-item/', RandomItem.as_view()),
    path('items/', Items.as_view()),
    path('items-views/', ItemsViews.as_view()),
    path('item/<int:id>/', Item.as_view()),
    path('item/<int:id>/view/', ItemViews.as_view()),
    path('item/<int:id>/rating/', RatingItem.as_view()),
]
