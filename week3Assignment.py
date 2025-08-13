original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage of the item:"))

def calculate_discount(original_price, discount_percentage):

    if discount_percentage > 20:
        final_amount = original_price - (original_price * (discount_percentage / 100))
        print(f"Pay {final_amount} for the item, you have a {discount_percentage}% discount." ) 
    else:
        print(f"Pay {original_price} for the item. No discount applied!")

calculate_discount(original_price, discount_percentage)
