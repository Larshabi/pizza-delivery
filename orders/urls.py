from django.urls import path
from .views import OrderCreateListView, OrderDetailView, UpdateOrderStatus, UserOrderView, UsersOrderView, UserOrderDetail
urlpatterns = [
    path('', OrderCreateListView.as_view()),
    path('<int:id>/', OrderDetailView.as_view()),
    path('update-status/<int:id>/', UpdateOrderStatus.as_view()),
    path('user/orders',UserOrderView.as_view()),
    path('user/<int:user_id>/orders', UsersOrderView.as_view()),
    path('user/<int:orderId>/',UserOrderDetail.as_view())
]