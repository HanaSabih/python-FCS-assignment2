# Write a function that counts the digits of a given number recursively.
# Ex : input= 123 output : 3, input 10000 output :5

# List Jumps
# You are given a list jumps of positive and negative integers which signify forward or negative jumps.

# Starting at index 0, you jump to index 0+jump[0]. In general, if you are at index k, you would jump to
# index k+jump[k] Let’s say jumps[0] was +2. Index becomes 2. Assuming jumps[2] was -1, index would
# become 1.

# Write the function list_jumps(jumps) where jumps is the aforementioned list. The function should
# return the string “cycle” if the index will never leave the boundaries of the input list otherwise it must
# return “out-of-bounds&amp;”. The starting index is always 0.

# POS for aamo el dekanje
# You want to write a POS system (point of service) to your neighbor’s dekene.
# In this system, you keep track of the items available. The items have a barcode, a name, and a price.
# When the system starts, it asks your 3ammo l dekanje if he wants to start a new receipt.
# If he chooses yes, he will be prompted for an item barcode and the quantity the client purched. If he
# answers no, the system exits.
# After choosing “yes” and then inputting the barcode and the quantity, aamo l dekanje is asked if he
# would like to add another item to the list.
# If he answers yes, he is prompted again for the barcode and quantity of the item. He will keep getting
# this prompt until he answers no to the question.
# Once he answered no, you the system will display the receipt where each item will appear on a line
# along with the quantity purchased and the total cost of that item (quantity*unit price)
# And at the last line of the receipt, the system prints total along with the total amount.
# Once this receipt is printed, the system goes back to the first step and asks aamo l dekane if he would
# like to start a new receipt.

# Use functions.



##################################################################################



def find_item_barcode(barcode, items):
    return items.get(barcode, None)

# Function to create a receipt
def create_receipt(items):
    receipt_items = []
    total = 0

    while True:
        barcode = input("Enter item barcode (or 'no' to finish): ")
        if barcode == 'no':
            break

        item = find_item_barcode(barcode, items)
        if item:
            quantity = int(input("Enter quantity purchased: "))
            receipt_items.append((item, quantity))
            total += item[2] * quantity
        else:
            print("Item not found.")

    print("\nReceipt:")
    for item, quantity in receipt_items:
        cost = item[2] * quantity
        print(f"{item[1]} - {quantity} x {item[2]} = {cost}")
    
    print("Total:", total)

# Main function
def main():
    items = {
        "123": ("123", "Item 1", 10),
        "456": ("456", "Item 2", 15),
        # Add more items
    }

    while True:
        start_receipt = input("Start a new receipt? (yes/no): ")
        if start_receipt.lower() == "no":
            break
        elif start_receipt.lower() == "yes":
            create_receipt(items)
        else:
            print("Invalid input. Enter 'yes' or 'no'.")

main()