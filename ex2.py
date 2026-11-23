def ticket_total(count, price=12):
    return count*price
def final_price(count, is_school_group=False):
    if is_school_group == False:
        return ticket_total(count)
    else:
        return ticket_total(count)*0.75
print(final_price(count=3))
print(final_price(4, is_school_group=True))
print(ticket_total(2,price=15))
