from . import views
from django.urls import path, include




urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    ##Social
    path('social/', include('social_django.urls', namespace='social')),
    
    ##Auth
    #signup
    path('signup/',views.SignUp.as_view(),name="signup"),

    #login
    path('login/',views.LogIn.as_view(),name="login"),

    #logout
    path('logout/',views.LogOut.as_view(),name="logout"),    
    
    ##Manager
    #products
    path('manager/products/',views.ProductList.as_view(),name="product_list"),
    path('manager/products/<pk>/',views.ProductDetail.as_view(),name="product_detail"),
    path('manager/products/<pk>/', views.ProductCreate.as_view(),name="product_create"),
    path('manager/products/<pk>/', views.ProductUpdate.as_view(),name="product_update"),
    path('manager/products/<pk>/', views.ProductDelete.as_view(),name="product_delete"),
    #product_images
    path('manager/product_images/',views.ProductImageList.as_view(),name="product_image_list"),
    path('manager/product_images/<pk>/',views.ProductImageDetail.as_view(),name="product_image_detail"),
    path('manager/product_images/<pk>/', views.ProductImageCreate.as_view(),name="product_image_create"),
    path('manager/product_images/<pk>/', views.ProductImageUpdate.as_view(),name="product_image_update"),
    path('manager/product_images/<pk>/', views.ProductImageDelete.as_view(),name="product_image_delete"),

    ##API
    #products
    path('api/products/',views.APIProductCreateView.as_view(),name="api_product"),
    path('api/products/<pk>/',views.APIProductDetailView.as_view(),name="api_product"),
    #product_images
    path('api/product_images/',views.APIProductImageCreateView.as_view(),name="api_product_image"),
    path('api/product_images/<pk>/',views.APIProductImageDetailView.as_view(),name="api_product_image"),
]