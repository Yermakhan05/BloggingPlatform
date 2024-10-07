from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import user_registration, user_profile, edit_profile, follow_user, unfollow_user, create_profile

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('create-profile/<int:user_id>/', create_profile, name='create_profile'),
    path('profile/<int:user_id>/', user_profile, name='profile'),
    path('profile/<int:profile_id>/edit/', edit_profile, name='edit_profile'),
    path('follow/<int:follower_id>/<int:following_id>', follow_user, name='follow_user'),
    path('unfollow/<int:follower_id>/<int:following_id>', unfollow_user, name='unfollow_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
