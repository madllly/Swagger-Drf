from django.contrib import admin
from django.urls import path
from main.views import *
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/cars/', CarApiView.as_view()),  # Get All
    path('api/v1/cars/<int:pk>/', CarViewDetail.as_view()),  # Get<id>
    path('api/v1/cars/create/', CarCreate.as_view()),  # Post
    path('api/v1/cars/<int:pk>/delete/', CarDelete.as_view()),  # Delete
    path('api/v1/cars/<int:pk>/update/', CarUpdate.as_view()),  # Put

    path('api/v1/clients/', ClientApiView.as_view()),
    path('api/v1/clients/<int:pk>/', ClientViewDetail.as_view()),
    path('api/v1/clients/create/', ClientCreate.as_view()),
    path('api/v1/clients/<int:pk>/delete/', ClientDelete.as_view()),
    path('api/v1/clients/<int:pk>/update/', ClientUpdate.as_view()),

    path('api/v1/workers/', WorkerApiView.as_view()),
    path('api/v1/workers/<int:pk>/', WorkerViewDetail.as_view()),
    path('api/v1/workers/create/', WorkerCreate.as_view()),
    path('api/v1/workers/<int:pk>/delete/', WorkerDelete.as_view()),
    path('api/v1/workers/<int:pk>/update/', WorkerUpdate.as_view()),

    path('api/v1/list-of-work/', ListOfWorkApiView.as_view()),
    path('api/v1/list-of-work/<int:pk>/', ListOfWorkViewDetail.as_view()),
    path('api/v1/list-of-work/create/',ListOfWorkCreate.as_view()),
    path('api/v1/list-of-work/<int:pk>/delete/', ListOfWorkDelete.as_view()),
    path('api/v1/list-of-work/<int:pk>/update/', ListOfWorkUpdate.as_view()),

    path('api/v1/order-list/', OrderListApiView.as_view()),
    path('api/v1/order-list/<int:pk>/', OrderListViewDetail.as_view()),
    path('api/v1/order-list/create/', OrderListCreate.as_view()),
    path('api/v1/order-list/<int:pk>/delete/', OrderListDelete.as_view()),
    path('api/v1/order-list/<int:pk>/update/', OrderListUpdate.as_view()),
]


urlpatterns += doc_urls