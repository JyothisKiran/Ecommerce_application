from django.urls import path
from .views import ShoeListView,ShoeDetailView,ShoeCheckoutView,SearchResultsView,home,BuyShoeView,ShoeOrderView,CustomLoginView,RegisterPage,orderfromcart,cart,remove_from_cart,add_to_cart,add_to_order

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name="register"),
    path('',home,name='home'),


    path('listshoes/',ShoeListView.as_view(),name='shoeslist'),
    path('detail/<int:pk>/', ShoeDetailView.as_view(),name='detail-view'),



    path('checkout/<int:pk>/', ShoeCheckoutView.as_view(),name='checkout-view'),
    # path('complete', views.PaymentComplete,name='complete'),
    path('search/',SearchResultsView.as_view(),name='search'),

    path('buyshoe/<int:pk>',add_to_order,name="buy-shoe"),
    path('orderlist/',ShoeOrderView.as_view(),name='orderlist'),



    path('cart/',cart,name ='cart'),
    path('addcart/<int:pk>',add_to_cart,name='addcart'),
    path('deletecart/<int:pk>',remove_from_cart,name='deletecart'),
    # path('cart/',ViewCart.as_view(),name='cart'),
    # path('addcart/<int:pk>',AddtoCart,name='addcart'),
    # path('deletecart/<int:pk>',DeleteCart.as_view(),name='deletecart'),
    path('orderfromcart/<int:pk>',orderfromcart,name='ordercart'),


]
