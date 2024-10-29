from .views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("cars/", cars, name="cars"),
    path("companies/", companies, name="companies"),
    path("get_car/<int:pk>/", get_car, name="get_car"),
    path("get_company/<int:pk>/", get_company, name="get_company"),
    path("add_car/", add_car, name="add_car"),
    path("add_company/", add_company, name="add_company"),
    path("update_car/<int:pk>", update_car, name="update_car"),
    path("update_company/<int:pk>",update_company, name="update_company"),
    path("delete_car/<int:pk>", delete_car, name="delete_car"),
    path("delete_company/<int:pk>", delete_company, name="delete_company"),
]
