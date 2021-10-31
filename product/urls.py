from django.urls import path

from .views import ProductListView, ProductDeatiledView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDeatiledView.as_view())
]