from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListCreate.as_view(), name="product-list"),
    path("products/delete/<int:pk>/",
         views.ProductDelete.as_view(), name="delete-product"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("login2/", views.login_view2, name="login2"),
]
