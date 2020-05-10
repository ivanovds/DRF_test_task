"""Admin interface"""

from django.contrib import admin
from api.profiles.models import Profile


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "birth_date", "location"]
    # list_filter = [""]
    # search_fields = ["user"]

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileModelAdmin)

