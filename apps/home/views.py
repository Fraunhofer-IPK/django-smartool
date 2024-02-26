# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import json
import requests



@login_required(login_url="/login/")
def index(request):
    r = requests.get('https://stickntrack.sensolus.com/rest/api/v2/devices/W4GU2J/data/aggregated/location/latest?apiKey=2fcc0c5d4181422ca5f8272938e96b9f')
    if r.status_code != 200:
        raise Exception ('Failed requesting location of device W4GU2J')
    pos = json.loads(r.text)
    print(json.dumps(r.text))
    html_template = loader.get_template('home/index.html')
    context = {'segment': 'index', 'lng': pos['lng'], 'lat': pos['lat']}
    return HttpResponse(html_template.render(context, request)) 


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
