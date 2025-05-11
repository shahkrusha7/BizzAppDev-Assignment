"""
Electricity Bill Calculation (Slab-wise Pricing)

Problem:
Calculate the electricity bill based on usage using the following slab rates:
0-100 units @ ₹5/unit
101-300 units @ ₹7/unit
301-500 units @ ₹10/unit
Above 500 units @ ₹15/unit

Approach:
1. Accept electricity usage in kWh from the user.
2. Calculate charges for each slab as applicable.
3. Display a clear bill breakdown and total amount.
"""

def calculate_bill(units):
    total=0
    if units>500:
        above=units-500
        total+=above*15
        print(f"501-{units} units @ 15/unit = {above*15}")
        units=500
    if units>300:
        slab=units-300
        total+=slab*10
        print(f"301-500 units @ 10/unit = {slab*10}")
        units=300
    if units>100:
        slab=units-100
        total+=slab*7
        print(f"101-300 units @ 7/unit = {slab*7}")
        units=100
    if units>0:
        total+=units*5
        print(f"0-100 units @ 5/unit = {units*5}")
    print(f"Total Amount Payable = ₹{total}")

usage=int(input("Enter electricity usage in kWh: "))
print("Electricity Bill:")
calculate_bill(usage)
