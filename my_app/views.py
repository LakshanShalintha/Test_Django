from django.http import HttpResponse
from django.template import loader

def members(request):
    members_list = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown']
    context = {
        'members': members_list,
    }
    template = loader.get_template('my_app/members.html')
    return HttpResponse(template.render(context, request))
