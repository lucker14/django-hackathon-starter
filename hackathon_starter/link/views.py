from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from link.models import Link, BoxObj
from link.forms import NewLinkForm

# Create your views here.
def create_new_link(request):
    return render(request, 'links/create.html', {})


def links_overview(request):
    links = BoxObj.objects.all()
    print(links)
    print(request.session)
    for key in request.session.keys():
        print "key:=>" + str(request.session[key])
    context = {'links': links}
    return render(request, 'links/dashboard.html', context)


def create_link(request):
    if request.method == 'POST':
        link_form = NewLinkForm(data=request.POST)
        if link_form:
            link = link_form.save()
            return HttpResponseRedirect('/link/dashboard/')
    else:
        return HttpResponseRedirect('/hackathon/api/')

# username = request.POST.get('username')
# password = request.POST.get('password')


def delete_link(request):
    to_delete_id = request.GET.get('id')

    link = BoxObj.objects.get(pk=to_delete_id)
    if link:
        link.delete()
        return HttpResponseRedirect('/link/dashboard/')
    else:
        return HttpResponseRedirect('/hackathon/api/')