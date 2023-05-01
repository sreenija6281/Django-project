from django.urls import path
from .views import WorkList, RegisterUser

urlpatterns = [
    path('api/works/', WorkList.as_view()),
    path('api/register/', RegisterUser.as_view()),
]
