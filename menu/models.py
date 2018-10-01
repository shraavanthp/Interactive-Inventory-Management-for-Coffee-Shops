from django.db import models

class Item_hdr(models.Model):
    SNACK = 'S'
    DRINK = 'D'
    TYPE = (
        (SNACK, 'Snack'),
        (DRINK, 'Drink'),
    )
    item_name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=1, choices=TYPE, default=DRINK)
    
    def __str__(self):
        return self.item_name

    @staticmethod
    def get_snacks():
        snack_list = Item_hdr.objects.filter(item_type='S').order_by('id')
        return snack_list

    @staticmethod
    def get_drinks():
        drink_list = Item_hdr.objects.filter(item_type='D').order_by('id')
        return drink_list


class Item_ingredients(models.Model):
    item = models.ForeignKey(Item_hdr, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredient

class Related_items(models.Model):
    item = models.ForeignKey(Item_hdr, on_delete=models.CASCADE, related_name='item_hdr_key')
    related_item = models.ForeignKey(Item_hdr, on_delete=models.CASCADE, related_name='related_items')

    def __str__(self):
        return self.related_item.item_name
