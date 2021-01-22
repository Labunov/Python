from django.urls import path
from .views import index, profile, BBlogoutView,RegisterUserView,RegisterDoneView
from .views import BBLoginViews, ChangeUserInfoView, BBPasswordChangeView

app_name='main'

urlpatterns = [
    path('',index, name = 'index'),
    path('accounts/register/done',RegisterDoneView.as_view(),name = 'register_done'),
    path('accounts/register/',RegisterUserView.as_view(), name = 'register'),
    path('accounts/login/',BBLoginViews.as_view(), name = "login"),
    path('account/profile/change/',ChangeUserInfoView.as_view(), name = 'profile_change'),
    path('accounts/profile/', profile, name= 'profile'),
    path('accounts/logout/',BBlogoutView.as_view(),name = 'logout'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(),name = 'password_change'),


]