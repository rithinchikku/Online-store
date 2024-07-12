from django.urls import path
from .import views
urlpatterns = [


    # path('adminn/',views.index),
    path("adminn/",views.listbook,name='display'),
    path('create/',views.createbook,name='create'),

    path('detailsview/<int:book_id>/',views.detailsview,name='details'),
    path('updateview/<int:book_id>/',views.updateview,name='update'),
    path('deleteview/<int:book_id>/',views.deletebook,name='delete'),


    path('search/',views.search,name='search')

]