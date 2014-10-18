from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext


def home(request):
    return render_to_response('admin/home.html', {},
                context_instance=RequestContext(request))
