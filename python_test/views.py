from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from .forms import ClientSearchForm, ClientForm
from .models import Client

import json


def client_list(request, template_name):
    search_form = ClientSearchForm()
    context = {"form": search_form}
    return render(request, template_name, context=context)


def client_list_data(request):
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 10))
    order_by = request.GET.get('sort')
    order_type = request.GET.get('order', 'asc')
    search_params = request.GET.get('search_params')

    clients = Client.objects.all()

    if search_params:
        search_params = json.loads(search_params)
        search_params.pop('csrfmiddlewaretoken', None)
        search_params = {k+'__icontains': v for k, v in search_params.items() if v}
        clients = clients.filter(**search_params)

    if order_by:
        if order_type == 'desc':
            order_by = "-" + order_by
        clients = clients.order_by(order_by)
    clients = clients[offset:offset+limit]

    total = clients.count()
    output = {"rows": list(clients.values()), "total": total}
    return JsonResponse(output, safe=False)


# TODO: Can be handled using two class based view with correct PUT method for update.

def post_client(request, template_name, client_id=None):
    client = None
    if client_id:
        client = Client.objects.get(id=client_id)
    if request.method == "POST":
        form = ClientForm(data=request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect(reverse('client_list'))
    else:
        form = ClientForm(instance=client)

    context = {
        'form': form,
        'client': client
    }

    return render(request, template_name, context=context)
