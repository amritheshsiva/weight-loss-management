from django.urls import path
from weight import views
urlpatterns = [
    path('add-weight/',views.add_weight, name='add_weight'),
    path('weights/',views.weight_list,name='weight_list'),
    path('delete-weight/<int:id>/',views.delete_weight, name='delete_weight'),
    path('edit-weight/<int:id>/',views.edit_weight, name='edit_weight'),
    path('weight-difference/',views.weight_difference, name='weight_difference'),



]