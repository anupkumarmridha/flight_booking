from django.shortcuts import render
from .models import Schedule, Route

# Create your views here.
def homeView(request):
    routes = Route.objects.all()
    context = {
        "routes": routes,
    }
    return render(request, "home/index.html", context)


def AllRoutes(request):
    AllRoutes = Route.objects.all()
    context = {
        "AllRoutes": AllRoutes,
    }
    return render(request, "home/all_routes.html", context)


def allSchedules(request, pk):
    route = Route.objects.get(id=pk)
    AllSchedules = Schedule.objects.filter(route=route).order_by("source_departure_datetime")

    context = {
        "AllSchedules": AllSchedules,
        "route": route,
    }
    return render(request, "home/all_schedules.html", context)

