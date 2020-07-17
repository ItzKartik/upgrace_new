from django.contrib import admin
from follow_app import models

admin.site.register(models.insta_id)
admin.site.register(models.join_us)
admin.site.register(models.contact_us)


class Used_Inline(admin.TabularInline):
    model = models.left_id


@admin.register(models.used_by)
class Main_Admin(admin.ModelAdmin):
    inlines = [
        Used_Inline
    ]
