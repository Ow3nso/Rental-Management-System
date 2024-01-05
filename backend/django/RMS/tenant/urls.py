# ----- 3rd Party Libraries -----
from django.urls import path

# ----- In-Built Libraries -----
from tenant import views

# ----- URL endpoints -----
tenant_list = views.TenantViews.as_view({
    'post': 'create',
    'get': 'list',
})
tenant_detail = views.TenantViews.as_view({
    'get': 'retrieve',
    'put': 'update',
})

urlpatterns = [
    path("tenant", tenant_list, name='tenant_list'),
    path('tenant/<int:pk>', tenant_detail, name="tenant_detail"),
]