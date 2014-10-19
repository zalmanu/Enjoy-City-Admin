from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Location
from .forms import LocationForm


@login_required
def home(request):
    print request.user.id
    locations = Location.objects.filter(user=request.user.id)
    return render_to_response('admin/home.html', {
                'locations' : locations
                }, context_instance=RequestContext(request))

@login_required
def location(request, location_id):
    if request.method == 'POST':
        form = LocationForm(request.POST, user=request.user.id)
        if form.is_valid():
            print 'VALID form, saving data.'
            form.save()
        else:
            print 'INVALID form data.'
    else:
        try:
            location = Location.objects.get(id=location_id)
            location_form = LocationForm(instance=location)
            return render_to_response('admin/location.html', {
                        'location_form': location_form
                        }, context_instance=RequestContext(request))
        except Location.DoesNotExist:
            # TODO: render a nice 404 page
            return HttpResponse('Not found')


