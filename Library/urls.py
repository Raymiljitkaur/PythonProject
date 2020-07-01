from django.conf.urls import url, include
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
#from .views import list_books, create_book, update_book, delete_book, issue_book, list_issuebook, delete_issuebook
from Library import views

urlpatterns = [
   
    #URLs general
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),

    #URLS for books 
    path('books', views.list_books, name='list_books'),
    path('newbook', views.create_book, name='create_books'),
    path('updatebook/<int:id>/', views.update_book, name='update_book'),
    path('deletebook/<int:id>/', views.delete_book, name='delete_book'),

 	#URLS for categories 
    path('categories', views.list_categories, name='list_categories'),
    path('newcategory', views.create_category, name='create_category'),
    path('updatecategory/<int:id>/', views.update_category, name='update_category'),
    path('deletecategory/<int:id>/', views.delete_category, name='delete_category'),


 	#URLS for publishers
    path('publishers', views.list_publishers, name='list_publishers'),
    path('newpublisher', views.create_publisher, name='create_publisher'),
    path('updatepublisher/<int:id>/', views.update_publisher, name='update_publisher'),
    path('deletepublisher/<int:id>/', views.delete_publisher, name='delete_publisher'),
   
    # urls for issue book
    path('issuedbooks/', views.list_issuebook, name='issuedbooks'),
    path('issuebook_create/', views.issue_book, name='issuebook_create'),
    path('update_bookissue/<int:id>/', views.issue_book, name='update_issuebook'),
    path('delete_bookissue/<int:id>/', views.delete_issuebook, name='delete_issuebook'),


    # URLS for Patrons
    path('patrons', views.list_patrons, name='list_patrons'),
    path('newpatron', views.create_patron, name='create_patrons'),
    path('updatepatron/<int:id>/', views.update_patron, name='update_patron'),
    path('deletepatron/<int:id>/', views.delete_patron, name='delete_patron'),
]


