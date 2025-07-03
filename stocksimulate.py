buy_orders = [
    {"qty": 1216, "price": 830},
    {"qty": 97, "price": 830},
    {"qty": 34, "price": 830},
    {"qty": 130, "price": 830},
    {"qty": 178, "price": 830},
]

sell_orders = [
    {"qty": 6388, "price": 840},
    {"qty": 55000, "price": 850},
    {"qty": 100000, "price": 850},
    {"qty": 126, "price": 850},
]

# Match orders
for buy in buy_orders:
    for sell in sell_orders:
        if buy["price"] >= sell["price"]:
            traded_qty = min(buy["qty"], sell["qty"])
            print(f"Matched: {traded_qty} units @ {sell['price']}")
            buy["qty"] -= traded_qty
            sell["qty"] -= traded_qty
            if buy["qty"] == 0:
                break

print("\nRemaining Buy Orders:")
for b in buy_orders:
    if b["qty"] > 0:
        print(b)

print("\nRemaining Sell Orders:")
for s in sell_orders:
    if s["qty"] > 0:
        print(s)
