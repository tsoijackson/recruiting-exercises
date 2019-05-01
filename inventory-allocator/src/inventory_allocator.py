from collections import defaultdict

# Assumptions I have made:
# 1. I assume that if an order can be partially allocated, but not fully allocated, then the solution will be empty
# 1. I assume I can mutate/change the input values of the function.
# 2. I assume that there will be no negative quantities of items. Example: {'apple': -5 }

# Solution Analysis: Greedy Algorithm -- take as much quantity possible in each warehouse until order is fully allocated or fullfilled
# Runtime: O(total_warehouses * total_items_in_order)
# Space: O(total_warehouses * total_items_in_warehouse)

class InventoryAllocator:

    def allocate_order(self, order, warehouses: ["Warehouse"]) -> [dict]:
        allocated_order = defaultdict(dict)

        for warehouse in warehouses:
            if warehouse.inventory:
                for item, quantity_needed in tuple(order.items()):
                    if item in warehouse.inventory:

                        quantity_ordered = min(quantity_needed, warehouse.inventory[item])
                        
                        # update order and warehouse inventory
                        warehouse.inventory[item] -= quantity_ordered
                        order[item] -= quantity_ordered

                        # update allocated order
                        if quantity_ordered > 0:
                            allocated_order[warehouse.name][item] = quantity_ordered

                        # remove item from order if item can be fully allocated
                        if order[item] == 0:
                            del order[item]

        # if there are no more items in order, then it can be fully allocated
        if len(order) == 0:
            return [ { key : value } for key,value in allocated_order.items() ]
        else:
            return [ ]