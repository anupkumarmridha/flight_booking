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
    list_filter=('arrival_location','departure_location','travel_time',)
    
class StopAdmin(admin.ModelAdmin):
    search_fields=('location',)
    list_filter=('route__departure_location','route__arrival_location','route__travel_time','arrival_time', 'departure_time','duration',)
class ScheduleAdmin(admin.ModelAdmin):
    search_fields=('flight__name', 'flight__flight_no', 'route__departure_location', 'route__arrival_location',)
    list_filter=('flight__name', 'flight__flight_no','route__departure_location','route__arrival_location','total_available_seats_on_flight','route__travel_time','arrival_time', 'departure_time','duration',)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Stop, StopAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Seat, SeatAdmin)
