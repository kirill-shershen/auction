from django.urls import path, include
from .views import AnimalView, LotView, BidView, UserView, BidAcceptView
from rest_framework import routers

app_name = "app"

router = routers.DefaultRouter()
router.register('animals', AnimalView)
router.register('lots', LotView)
router.register('bids', BidView)
router.register('users', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('bids/<int:pk>/accept/', BidAcceptView.as_view())
]
