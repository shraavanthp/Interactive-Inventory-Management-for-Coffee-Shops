from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
import pdb

from menu.models import Item_hdr


def index(request):
    template = loader.get_template('menu/index.html')
    context = {'snack_list' : Item_hdr.get_snacks(), 'drinks_list' : Item_hdr.get_drinks()}
    return HttpResponse(template.render(context, request))


def item_detail(request, item_id):
    item = Item_hdr.objects.get(id=item_id)
    template = loader.get_template('menu/item_detail.html')
    context = {'item': item}
    return HttpResponse(template.render(context, request))


def detail(request):
    item_list = Item_hdr.objects.all
    template = loader.get_template('menu/detail.html')
    context = {'item_list': item_list}
    return HttpResponse(template.render(context, request))


def save(request):
    #pdb.set_trace()
    item_name = request.POST['item_name']
    item_type = request.POST['type']
    ingredient = request.POST.getlist('ingredients[]')
    temp = Item_hdr(item_name=item_name, item_type=item_type)
    temp.save()
    for ing in reversed(ingredient):
        temp.item_ingredients_set.create(ingredient=ing)
    rel = temp.item_hdr_key
    related = request.POST.getlist('related')
    for rel_id in related:
        rel.create(related_item=(Item_hdr.objects.get(id=rel_id)))
    return HttpResponseRedirect(reverse('menu:index'))


def delete(request, item_id):
    i = Item_hdr.objects.get(id=item_id)
    i.delete()
    return HttpResponseRedirect(reverse('menu:index'))


def edit(request, item_id):
    item_list = Item_hdr.objects.all
    template = loader.get_template('menu/edit.html')
    edit_item = Item_hdr.objects.get(id=item_id)
    list=[]
    for ei in edit_item.item_hdr_key.all():
        list.append(ei.related_item.id)
    context = {'item_list': item_list, 'edit_item': edit_item, 'related_list': list}
    return HttpResponse(template.render(context, request))


def edit_save(request, item_id):
    edit_item = Item_hdr.objects.get(id=item_id)
    edit_item.item_name = request.POST['item_name']
    edit_item.item_type = request.POST['type']
    edit_item.save()
    edit_item.item_ingredients_set.all().delete()
    edit_item.item_hdr_key.all().delete()
    ingredient = request.POST.getlist('ingredients[]')
    related = request.POST.getlist('related')
    for ing in ingredient:
        edit_item.item_ingredients_set.create(ingredient=ing)
    for rel_id in related:
        edit_item.item_hdr_key.create(related_item=(Item_hdr.objects.get(id=rel_id)))
    return HttpResponseRedirect(reverse('menu:index'))

#c.create(related_item=(Item_hdr.objects.get(id=1)))
