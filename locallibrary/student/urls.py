from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]


urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), #still working
]


# Add URLConf for librarian to renew a book.
urlpatterns += [   
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [  
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
]
