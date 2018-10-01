from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Item_hdr


class ItemHdrTests(TestCase):

    def test_get_snacks_works_with_no_snacks(self):
        """
        The count of objects returned by get_snacks()
        should return 0 when drinks are created.
        """
        self.assertIs(Item_hdr.get_snacks().count(), 0)
        i = Item_hdr(item_name='Coffee', item_type='D')
        i.save()
        self.assertIs(Item_hdr.get_snacks().count(), 0)

    def test_get_snacks_works_with_snacks(self):
        """
        The count of objects returned by get_snacks()
        should return the number of snacks created.
        """
        self.assertIs(Item_hdr.get_snacks().count(), 0)
        i = Item_hdr(item_name='Cake', item_type='S')
        i.save()
        self.assertIs(Item_hdr.get_snacks().count(), 1)
        i = Item_hdr(item_name='Bagel', item_type='S')
        i.save()
        self.assertIs(Item_hdr.get_snacks().count(), 2)

    def test_get_drinks_works_with_no_drinks(self):
        """
        The count of objects returned by get_drinks()
        should return 0 when snacks are created.
        """
        self.assertIs(Item_hdr.get_drinks().count(), 0)
        i = Item_hdr(item_name='Bagel', item_type='S')
        i.save()
        self.assertIs(Item_hdr.get_drinks().count(), 0)

    def test_get_drinks_works_with_drinks(self):
        """
        The count of objects returned by get_drinks()
        should return the number of drinks created.
        """
        self.assertIs(Item_hdr.get_drinks().count(), 0)
        i = Item_hdr(item_name='Coffee', item_type='D')
        i.save()
        self.assertIs(Item_hdr.get_drinks().count(), 1)
        i = Item_hdr(item_name='Tea', item_type='D')
        i.save()
        self.assertIs(Item_hdr.get_drinks().count(), 2)
