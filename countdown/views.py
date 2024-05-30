from django.shortcuts import render, redirect
from .models import Event
from django.utils import timezone

def home(request):
    upcoming_event = Event.objects.filter(event_datetime__gte=timezone.now()).order_by('event_datetime').first()
    upcoming_events = Event.objects.filter(event_datetime__gte=timezone.now()).order_by('event_datetime')[1:]
    return render(request, 'home.html', {'upcoming_event': upcoming_event, 'upcoming_events': upcoming_events})

def event_detail(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_datetime = request.POST.get('event_datetime')

        event = Event.objects.create(name=event_name, event_datetime=event_datetime)
        return redirect('home')
    
    return render(request, 'event_detail.html')
