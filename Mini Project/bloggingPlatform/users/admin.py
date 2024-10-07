from django.contrib import admin

from users.models import Profile, Follow


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Bio', 'ProfilePicture')
    search_fields = ('Bio',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following')
    search_fields = ('id',)
