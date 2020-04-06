from django.contrib import admin

from .models import Booking, Contact, Artist, Album


class BookingInline(admin.TabularInline):
    readonly_fields = ['created_at', 'contacted', 'album']
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
    ]
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

    def has_add_permission(self, request, obj):
        return False


class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'contact', 'album', 'contacted']
    list_filter = ['created_at', 'contacted']

    def has_add_permission(self, request):
        return False
