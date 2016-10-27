from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import jeepForm
from .models import Jeep
def jeepneys_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = jeepForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context={
        "form": form,
    }
    return render(request, "jeepneys_form.html", context)

def jeepneys_detail(request, id=None):
    instance = get_object_or_404(Jeep, id=id)
    context = {
        "route": instance.route,
        "instance": instance,
    }
    return render(request,"jeepneys_detail.html",context)
    

def jeepneys_list(request):
    queryset= Jeep.objects.all()
    query= request.GET.get("q")
    if query:
        queryset = queryset.filter(place__icontains=query)
    context = {
        "object_list": queryset,
        "route": "My route List"
    }
    return render(request,"jeepney_list.html",context)

def jeepneys_updated(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = jeepForm(request.POST or None, request.FILES or None)
    instance = get_object_or_404(Jeep, id=id)
    form = jeepForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item<a/> Saved",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "route": instance.route,
        "instance":instance,
        "form":form,
    }
    return render(request, "jeepneys_form.html", context)


def jeepneys_delete(request, id=None):
    instance = get_object_or_404(Jeep, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("list")
    