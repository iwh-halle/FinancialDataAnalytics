from django.urls import path
from .views import chart_data, chart_view

urlpatterns = [
    path('api/chart/', chart_data, name='chart_data'),
    path('chart/', chart_view, name='chart_view'),  # URL for the Chart.js visualization
    path('', chart_view, name='home_chart'),  # Make chart the landing page as well
]
