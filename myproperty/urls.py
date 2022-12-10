from django.urls import path
from .views import home_page, about, service, properties

urlpatterns = [
     path("", home_page, name="home_page"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    path("properties/", properties, name="properties")

]