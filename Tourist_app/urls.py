from django.urls import path
from .views import *


urlpatterns=[
    path('create/',CreateTouristPlace.as_view(),name="create-place"),
    path('view/<int:pk>/',ViewTouristPlace.as_view(),name="view-place"),
    path('update/<int:pk>/',UpdateTouristPlace.as_view(),name="update-place"),
    path('delete/<int:pk>/',DeleteTouristPlace.as_view(),name="delete-place"),


    path('adminreg/',RegisterAdmin.as_view(),name="admin-reg"),
    path('viewAdmin/<int:pk>/',ViewAdmin.as_view(),name="view-admin"),
    path('viewlogin/',ViewLogin.as_view(),name="view-login"),
    path('verifylogin/', VerifyLogin.as_view(), name="verify-login"),

]


