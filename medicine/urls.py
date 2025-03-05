from django.urls import path
from .views import home_page, MedicineList, MedicineCreate, MedicineDetail, MedicineUpdate, MedicineDelete

urlpatterns = [
    path('', home_page, name='home-page'),
    path('medicine_list/', MedicineList.as_view(), name='medicine-list'),
    path('medicine-detail/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
    path('medicine-update/<int:pk>/', MedicineUpdate.as_view(), name='medicine-update'),
    path('medicine-create/', MedicineCreate.as_view(), name='medicine-create'),
    path('medicine-delete/<int:pk>/', MedicineDelete.as_view(), name='medicine-delete'),
]