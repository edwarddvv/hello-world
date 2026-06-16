def calculate_total(price, quantity):
    return price * quantity


def display_total(total):
    print(f"The total is £{total}")


def generate_summary(total):
    return f"Summary: the final total is £{total}"


price = 5
quantity = 3
total = calculate_total(price, quantity)

display_total(total)
print(generate_summary(total))
