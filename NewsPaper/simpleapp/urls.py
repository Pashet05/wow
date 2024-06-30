from django.urls import path , include
# Импортируем созданное нами представление
from .views import NewsList, NewDetail, ProductsList, multiply, ProductsCreate, ProductsDetail, ProductsUpdate, \
   ProductsDelete, NewsCreate, NewsDelete, NewsUpdate, TopList, Author_now

urlpatterns = [
   path('', TopList.as_view(), name='top.html'),
   path('news/', NewsList.as_view(), name = 'news_list'),
   path('products/', ProductsList.as_view(),name='product_detail'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('news/<int:pk>', NewDetail.as_view(), name='news_detail'),
   path('products/<int:pk>', ProductsDetail.as_view(), name='product_detail'),
   path('multiply/', multiply),
   path('create/', ProductsCreate.as_view(), name='product_create'),
   path('<int:pk>/update/', ProductsUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductsDelete.as_view(), name='product_delete'),
   path('news/create/', NewsCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
   path("accounts/", include("allauth.urls")),
   path('author_now/', Author_now, name='author_now'),
]
