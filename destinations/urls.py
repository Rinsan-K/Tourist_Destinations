from django.urls import path
from .views import *

urlpatterns = [
    path('api/create/', DestinationCreateView.as_view(), name="api_create_destination"),
    path('api/detail/<int:pk>/', DestinationDetailView.as_view(), name="api_detail_destination"),
    path('api/list/', DestinationListView.as_view(), name="api_list_destination"),
    path('api/update/<int:pk>/', DestinationUpdateView.as_view(), name="api_update_destination"),
    path('api/delete/<int:pk>/', DestinationDeleteView.as_view(), name="api_delete_destination"),
    path('api/search/', DestinationSearchView.as_view(), name="api_search_destination"),

    path('create_destination/', create_destination, name="create_destination"),
    path('update_destination/<int:pk>/', update_destination, name="update_destination"),
    path('delete_destination/<int:pk>/', delete_destination, name="delete_destination"),
    path('detail_destination/<int:pk>/', destination_detail, name="destination_detail"),
    path('', index, name="index"),
]
