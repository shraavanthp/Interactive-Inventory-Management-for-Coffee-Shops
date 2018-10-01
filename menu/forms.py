from django import forms

from .models import Item_hdr

class ItemForm(forms.ModelForm):
    class meta:
        model = Item_hdr
        fields = ('item_name','item_type','related_items')
