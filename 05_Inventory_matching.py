"""
Inventory Matching and Pricing

Problem:
You have a list of products with quantities and unit prices. A customer places an order with a budget.
The program must determine:
- If the order can be fully fulfilled within budget,
- If only part of it can be fulfilled,
- Or if it's impossible due to insufficient inventory or too low a budget.

Approach:
1. Sort inventory by unit price (cheapest first).
2. Try to fulfill the order by buying as much as possible within budget.
3. Track total items bought and cost to determine outcome.
"""

def check_order(inventory,order_quantity,budget):
    inventory.sort(key=lambda x:x['price'])
    total_bought=0
    total_cost=0
    for item in inventory:
        if total_bought>=order_quantity:
            break
        available=item['quantity']
        price=item['price']
        needed=order_quantity-total_bought
        buy=min(available,needed)
        cost=buy*price
        if total_cost+cost<=budget:
            total_bought+=buy
            total_cost+=cost
        else:
            affordable=(budget-total_cost)//price
            total_bought+=affordable
            total_cost+=affordable*price
            break
    if total_bought==order_quantity:
        status="Order is fully fulfillable."
    elif total_bought>0:
        status="Order is partially fulfillable."
    else:
        status="Order is not fulfillable."
    return status,total_bought,total_cost

inventory=[
    {'name':'Product A','quantity':5,'price':10},
    {'name':'Product B','quantity':3,'price':5},
    {'name':'Product C','quantity':10,'price':15}
]

order_quantity=6
budget=50

status,bought,cost=check_order(inventory,order_quantity,budget)
print(status)
print(f"Total items bought: {bought}")
print(f"Total cost: {cost}")
