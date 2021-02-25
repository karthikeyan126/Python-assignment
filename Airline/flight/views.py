from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

def __index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, 'Airline/index.html', context)

def new_index(request):
    return render(request, 'Airline/new_index.html')

def index(request):
    return HttpResponse('hello from Airlines!!')


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight Does not exist")

    context = {
        "flight":flight,
        "Passenger":flight.Passenger.all(),
        "non_passenger": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, 'flight/flight.html', context)


def book(request, flight_id):
    try:
        Passenger_id = int(request.POST['Passenger'])
        passenger = Passenger.objects.get(pk=Passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flight/error.html", {"message": 'No Selections'})
    except Flight.DoesNotExist:
        return render(request, "flight/error.html", {"message": "No Flight."})
    except Passenger.DoesNotExist:
        return render(request, "flight/error.html", {"message": "No passenger"})

    Passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flight', args=(flight_id,)))


# Create your views here.
