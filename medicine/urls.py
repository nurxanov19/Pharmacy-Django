from django.urls import path
from .views import (home_page, MedicineList, MedicineCreate, MedicineDetail, MedicineUpdate, MedicineDelete,
                    MedicineApiList, MedicineApiCreate, MedicineApiUpdate, MedicineApiDetail, MedicineApiDelete)


urlpatterns = [
    path('#', home_page, name='home-page'),
    path('medicine_list/', MedicineList.as_view(), name='medicine-list'),
    path('medicine-detail/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
    path('medicine-update/<int:pk>/', MedicineUpdate.as_view(), name='medicine-update'),
    path('medicine-create/', MedicineCreate.as_view(), name='medicine-create'),
    path('medicine-delete/<int:pk>/', MedicineDelete.as_view(), name='medicine-delete'),
] + [
    path('', MedicineApiList.as_view(), name='lisp-api'),
    path('create-api/', MedicineApiCreate.as_view(), name='create-api'),
    path('update-api/<int:pk>', MedicineApiUpdate.as_view(), name='update-api'),
    path('detail-api/<int:pk>', MedicineApiDetail.as_view(), name='detail-api'),
    path('delete-api/<int:pk>', MedicineApiDelete.as_view(), name='delete-api'),

]