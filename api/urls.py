from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView, UserDashboard
from rest_framework_simplejwt import views as jwt_views
from native import views as nviews


urlpatterns = [
    url(r'^login/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^register/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^logout/$',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout'),
    url(r'^register/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^dashboard/$', nviews.index, name ='dashboard'),
]