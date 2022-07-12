from django.contrib import admin

from givito.account.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = [ 'email','name', 'is_active', 'created_at', 'modified_at', 'deleted_at',"is_staff","is_superuser",]
    search_fields = ["name", "email", "phone"]
    list_filter = ["is_active","is_staff","is_superuser","modified_at", "created_at", "deleted_at"]

admin.site.register(User, UserAdmin)