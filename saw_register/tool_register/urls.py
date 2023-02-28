from django.urls import path
from .views import *

urlpatterns = [
    path("", WorkPlaceView.as_view(), name="home"),
    path('saw_brands/<int:pk>', SawBrandView.as_view(), name='saw_brands'),
    path('saw/<int:pk>', SawView.as_view(), name='saw'),
    path('meters/<int:pk>', MetersView.as_view(), name='meters'),
    path('signup/', sign_up, name='signup'),
]