from django.urls import path
from .views import Index, History, News, InterestingPlaces


app_name = 'website'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('interesting_places/', InterestingPlaces.as_view(),
         name='interesting_places'),
    path('history/', History.as_view(), name='history'),
    path('news/', News.as_view(), name='news')
]
