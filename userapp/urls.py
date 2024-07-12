from django.urls import path
from .import views
urlpatterns = [



    path('userlist',views.userlist,name='userdisplay'),
    path('userdetails/<int:book_id>/',views.userdetails,name='userdetails'),
    path('usersearch/',views.usersearch,name='usersearch'),

    path('addtocart/<int:book_id>/',views.add_to_cart,name='cart'),
    path('viewcart/',views.view_cart,name='viewcart'),
    path('increase/<int:item_id>/',views.increase_quantity,name='increase'),
    path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease'),
    path('remove_from_cart/<int:item_id>/',views.remove_cart,name='remove_cart'),

    path('create_checkout_session/',views.create_checkout_session,name='create_checkout_session'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel'),

]