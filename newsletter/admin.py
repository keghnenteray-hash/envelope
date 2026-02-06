from django.contrib import admin
from . models import Subscriber

# Register your models here.

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
    ordering = ('-subscribed_at',)
    list_per_page = 25

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subscriber_count'] = Subscriber.objects.count()
        return super().changelist_view(request, extra_context=extra_context)