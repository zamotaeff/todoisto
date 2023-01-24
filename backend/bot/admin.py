from bot.models import TgUser
from django.contrib import admin


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "username", "user")
    readonly_fields = ("chat_id", "verification_code")
