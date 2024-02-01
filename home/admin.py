from django.contrib import admin
from home.models import (
    Flight,
    Route,
    Stop,
    Schedule,
    Seat,
)

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display=('name','flight_no',)
    list_filter=('capacity', 'type', 'name', 'flight_no',)
    
class SeatAdmin(admin.ModelAdmin):
    search_fields=('flight__flight_no',)
    list_filter=('flight_class','flight__name',)
    
class RouteAdmin(admin.ModelAdmin):
    list_filter=('arrival_location','departure_location','travel_time')
    
admin.site.register(Flight, FlightAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Stop)
admin.site.register(Schedule)
admin.site.register(Seat, SeatAdmin)
