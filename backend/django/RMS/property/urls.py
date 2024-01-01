# ----- 3rd Party Libraries -----
from django.urls import path

# ----- In-Built Libraries -----
from property import views

# ----- URL endpoints -----
property_list = views.PropertyView.as_view({
    'post': 'create',
    'get': 'list',
})
property_detail = views.PropertyView.as_view({
    'get': 'retrieve',
    'put': 'update',
})

urlpatterns = [
    path("property", property_list, name='property_list'),
    path('property/<int:pk>', property_detail, name="property_detail"),
]