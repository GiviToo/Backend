from django.contrib import admin

from givito.service.models import Category, Project, ProjectRegistrant

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["owner", "created_at", "modified_at", "status", "registrant"]
    search_fields = ["owner", "description"]

class ProjectRegistrantAdmin(admin.ModelAdmin):
    list_display = ["owner", "created_at", "modified_at", "project", "status"]
    search_fields = ["owner", "project", "description"]
    # list_filter = ["status"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectRegistrant, ProjectRegistrantAdmin)
admin.site.register(Category)