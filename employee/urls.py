from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeListAPIView.as_view(), name="employee"),
    path('<int:id>', views.EmployeeDetailAPIView.as_view(), name="employee"),
]