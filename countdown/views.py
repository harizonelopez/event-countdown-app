from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.utils import timezone
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse

def home(request):
    now = timezone.localtime(timezone.now())

    upcoming_events = Event.objects.filter(event_datetime__gte=now).order_by('event_datetime')

    events_json = json.dumps(
        list(upcoming_events.values('id', 'name', 'event_datetime')),
        cls=DjangoJSONEncoder
    )

    return render(request, 'home.html', {'upcoming_events': upcoming_events, 'events_json': events_json})

def event_detail(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        event_datetime = request.POST.get('event_datetime')

        event_datetime = timezone.make_aware(timezone.datetime.fromisoformat(event_datetime))

        Event.objects.create(name=event_name, event_datetime=event_datetime)
        return redirect(reverse('home'))
    
    return render(request, 'event_detail.html')

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('home')
