from rest_framework import routers
from auth_app.views import UsersView, authenticated_user, CreateUserView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.DefaultRouter()
router.register(r'users', UsersView, basename="users")

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('create-user', CreateUserView.as_view(), name="create-user"),
    path('authenticated_user/', authenticated_user, name="authenticated_user"),
]

urlpatterns += router.urls
