from django.urls import path
from .views import SensorView, SensorDetailView, SensorCreateView, SensorUpdateView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensor/<pk>/', SensorDetailView.as_view()),
    path('sensors_create/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
