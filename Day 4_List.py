A list stores many items in one place

fruits = ["apple", "mango", "banana"]

1. Add an item
fruits.append("orange")

2. Remove an item
fruits.remove("banana")

3. Access by index (counting starts from 0)
print(fruits[0])  # apple

4. Change an item
fruits[1] = "pineapple"

5. Loop through the list
for fruit in fruits:
    print(f"I like {fruit}")

print("Final list:", fruits)
