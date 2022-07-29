from django.urls import path
from .views import OrderCreateListView, OrderDetailView, UpdateOrderStatus
urlpatterns = [
    path('', OrderCreateListView.as_view()),
    path('<int:id>/', OrderDetailView.as_view()),
    path('update-status/<int:id>/', UpdateOrderStatus.as_view())
]