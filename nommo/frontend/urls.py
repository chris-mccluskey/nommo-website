from django.urls import path
from django.conf.urls import include

from . import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.HomeView.as_view(), name='index'),
    path('investments/', views.InvestmentsView.as_view(), name='investments'),
    path('investments/<int:pk>/', views.InvestmentView.as_view(), name='investment_by_id'),
    path('create_investment/', views.CreateInvestmentView.as_view(), name='create_investment'),
    path('edit_investment/<int:pk>/', views.EditInvestmentView.as_view(), name='edit_investment'),
    path('delete_investment/<int:pk>', views.DeleteInvestmentView.as_view(), name='delete_investment'),
    # path('favorites/', views.FavoritesView.as_view(), name='favorites'),
    # path('add-to-favorites/', views.AddFavorite.as_view(), name='add_to_favorites'),
    # path('remove-from-favorites/', views.RemoveFavorite.as_view(), name='remove_from_favorites'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
