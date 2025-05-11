"""
Bank Transaction Analyzer (Representation & Clarity)

Problem:
Allow users to input a series of bank transactions (credits and debits),
record each transaction, show balance updates, and provide a final summary.

Approach:
1. Accept transactions as input (type and amount).
2. Update and show balance after each transaction.
3. Print a final summary of total credits, debits, and ending balance.
"""

def analyze_transactions():
    transactions=[]
    balance=0
    while True:
        entry=input("Enter transaction (credit/debit amount), or 'done' to finish: ")
        if entry.lower()=='done':
            break
        try:
            ttype,amount=entry.split()
            amount=float(amount)
            if ttype.lower()=='credit':
                balance+=amount
                transactions.append((ttype,amount,balance))
            elif ttype.lower()=='debit':
                balance-=amount
                transactions.append((ttype,-amount,balance))
            else:
                print("Invalid transaction type. Use 'credit' or 'debit'.")
        except:
            print("Invalid format. Use: credit 100 or debit 50")

    print("\nTransaction Summary:")
    total_credit=sum(t[1] for t in transactions if t[1]>0)
    total_debit=-sum(t[1] for t in transactions if t[1]<0)
    for t in transactions:
        print(f"{t[0].capitalize():6} ₹{abs(t[1]):.2f} => Balance: ₹{t[2]:.2f}")
    print(f"\nTotal Credit: ₹{total_credit:.2f}")
    print(f"Total Debit: ₹{total_debit:.2f}")
    print(f"Final Balance: ₹{balance:.2f}")

analyze_transactions()
