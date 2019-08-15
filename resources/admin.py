from django.contrib import admin

from .models import Room, Rack, Subject, ResourceType


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    pass
