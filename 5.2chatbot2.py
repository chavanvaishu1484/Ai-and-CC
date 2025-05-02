def clothingShopBot():
    print("Enter your name: ", end="")
    name = input()
    print(f"\nHello {name}, welcome to Simple Clothing Store!\n")

    clothes = ["T-Shirt", "Jeans", "Jacket", "Dress", "Sneakers"]
    prices = [500, 1200, 2000, 1500, 2500]
    quantity = [0] * len(clothes)

    while True:
        print("\nAvailable Items:")
        for i in range(len(clothes)):
            print(f"{i + 1}. {clothes[i]} - Rs.{prices[i]}")

        choice = int(input("\nEnter the option number to buy: "))
        if 1 <= choice <= len(clothes):
            quantity[choice - 1] += 1
            print(f"Added {clothes[choice - 1]} to your cart.")
        else:
            print("Invalid option. Try again.")
            continue

        more = input("Do you want to buy more? (yes/no): ").lower()
        if more != "yes":
            break

    print("\nYour Order:")
    total = 0
    for i in range(len(clothes)):
        if quantity[i] > 0:
            print(f"{clothes[i]} x {quantity[i]}")
            total += quantity[i] * prices[i]

    print(f"\nTotal Bill: Rs.{total}")
    print("Thank you for shopping with us!")


if __name__ == "__main__":
    clothingShopBot()
