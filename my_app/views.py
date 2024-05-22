from django.http import HttpResponse
from django.template import loader


def members(request, template):
    template = loader.get_template('lak.html')
    return HttpResponse(template.render())
