from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('data/sesar/', views.get_sesar_data, name='sesar_data'),
    path('data/subduksi/', views.get_subduksi_data, name='subduksi_data'),
]
