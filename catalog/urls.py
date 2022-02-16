from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # adding my own code for password reset here
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

