from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AccountViewSet, CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"transactions", TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "accounts/<int:pk>/balance/",
        AccountViewSet.as_view({"get": "balance"}),
        name="account-balance",
    ),
    path(
        "transactions/spent_by_category/",
        TransactionViewSet.as_view({"get": "spent_by_category"}),
        name="spent-by-category",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
