from django.contrib import admin

from goals.models import GoalCategory, Goal


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "created", "updated", "due_date")
    search_fields = ("title", "user")


admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalCategory, GoalCategoryAdmin)
