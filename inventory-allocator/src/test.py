import unittest
from warehouse import Warehouse
from inventory_allocator import InventoryAllocator

# Assumptions:
# 1. I assume that in the list of warehouses as the second input, warehouses cannot have the same name

class TestInventoryAllocator(unittest.TestCase):

    def test_not_enough_inventory_for_single_item(self):
        # no warehouses
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10}, []) )

        # warehouse object is null
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse() ]) )

        # warehouse exist, but does not have item
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item2': 10}) ]) )

        # not enough quantity in a single warehouse
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 5}) ]) )

        # not enough quantity in a multiple warehouses
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 5}), Warehouse('wh2', {'item1': 2}), Warehouse('wh3', {'item1': 2}) ]) )


    def test_not_enough_inventory_for_multiple_items(self):
        # no warehouses
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10, 'item2': 10}, []) )

        # warehouse object is null
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10, 'item2': 10}, [ Warehouse() ]) )

        # warehouse exist, but does not have item
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10, 'item2': 10}, [ Warehouse('wh1', {'item2': 10}) ]) )

        # not enough quantity in a single warehouse
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10, 'item2': 10}, [ Warehouse('wh1', {'item1': 5}) ]) )

        # not enough quantity in a multiple warehouses
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10, 'item2': 10}, [ Warehouse('wh1', {'item1': 5}), Warehouse('wh2', {'item1': 2}), Warehouse('wh3', {'item1': 2}) ]) )

        # enough quantity in for an item, but not the rest of the order
        self.assertEqual([], InventoryAllocator().allocate_order({'item1': 10, 'item2': 10}, [ Warehouse('wh1', {'item1': 5}), Warehouse('wh2', {'item1': 5}), Warehouse('wh3', {'item1': 5}) ]) )

    
    def test_enough_inventory_for_single_item(self):
        # single warehouse with single item in inventory -- exact quantity
        self.assertEqual([{'wh1' : {'item1': 10}}], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 10}) ]))

        # single warehouse with single item in inventory -- over quantity
        self.assertEqual([{'wh1' : {'item1': 10}}], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 20}) ]))

        # multiple warehouses -- multiple items in inventory -- over quantity in first warehouse
        self.assertEqual([{'wh1' : {'item1': 10}}], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 10}), Warehouse('wh2', {'item1': 20}) ]))

        # multiple warehouses -- multiple items in inventory -- not enough quantity in first warehouse
        self.assertEqual([{'wh1' : {'item1': 4}}, {'wh2' : {'item1': 6}}], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 4}), Warehouse('wh2', {'item1': 20}) ]))

        # multiple warehouses -- exact quantity needed
        self.assertEqual([{'wh1' : {'item1': 4}}, {'wh2' : {'item1': 6}}], InventoryAllocator().allocate_order({'item1': 10}, [ Warehouse('wh1', {'item1': 4}), Warehouse('wh2', {'item1': 6}) ]))


    def test_enough_inventory_for_multiple_items(self):
        # single warehouse with exact quantity
        self.assertEqual([{'wh1' : {'item1': 10, 'item2':10}}], InventoryAllocator().allocate_order({'item1': 10, 'item2':10}, [ Warehouse('wh1', {'item1': 10, 'item2':10}) ]))

        # single warehouse with over quantity
        self.assertEqual([{'wh1' : {'item1': 10, 'item2':10}}], InventoryAllocator().allocate_order({'item1': 10, 'item2':10}, [ Warehouse('wh1', {'item1': 20, 'item2':20}) ]))

        # multiple warehouses -- multiple items in inventory -- over quantity in first warehouse
        self.assertEqual([{'wh1' : {'item1': 10, 'item2':10}}], InventoryAllocator().allocate_order({'item1': 10, 'item2':10}, [ Warehouse('wh1', {'item1': 20, 'item2':20}), Warehouse('wh2', {'item1': 20, 'item2':20}) ]))

        # multiple warehouses -- multiple items in inventory -- not enough quantity in first warehouse
        self.assertEqual([{'wh1' : {'item1': 4, 'item2': 5}}, {'wh2' : {'item1': 6, 'item2': 5}}], InventoryAllocator().allocate_order({'item1': 10, 'item2':10}, [ Warehouse('wh1', {'item1':4, 'item2':5}), Warehouse('wh2', {'item1': 20, 'item2':20}) ]))

        # multiple warehouses -- exact quantity needed
        self.assertEqual([{'wh1' : {'item1': 4, 'item2': 5}}, {'wh2' : {'item1': 6, 'item2': 5}}], InventoryAllocator().allocate_order({'item1': 10, 'item2':10}, [ Warehouse('wh1', {'item1':4, 'item2':5}), Warehouse('wh2', {'item1': 6, 'item2':5}) ]))



if __name__ == '__main__':
    unittest.main(verbosity = 2)