from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserView)
router.register('products2', views.ProductViewSet)
router.register('company2', views.CompanyViewSet)

urlpatterns = [
    path('products/', views.product_list),
    path('product', views.add_product),
    path('product/<int:pk>', views.get_product),
    path('seller', views.SellerView.as_view()),
    path('company', views.CompanyListView.as_view()),
    path('company/<int:pk>', views.CompanyView.as_view()),
    path('', include(router.urls))
]