# 🧾 Simple Billing System (Python CLI)

A basic Python console application to generate bills for customers by calculating the total amount based on quantity and price of items.

---

## 📌 Features

* Takes customer name as input
* Allows entering product details
* Supports multiple items per customer
* Calculates total bill amount
* Displays formatted bill summary
* Handles multiple customers using loop

---

## ⚙️ How It Works

1. Enter customer name
2. Enter product name
3. Add:

   * Quantity
   * Price (amount per item)
4. Program calculates total:

   ```
   total += quantity × amount
   ```
5. Repeat for multiple items
6. Displays final bill
7. Option to move to next customer

---

## ▶️ Usage

Run the script:

```bash
python billing_system.py
```

Follow the prompts to:

* Enter customer details
* Add items
* View total bill

---

## 🖥️ Example Output

```
enter the name : Rahul
enter the product name : Groceries
enter the quantity : 2
enter the amount : 100
do you want to add more items (yes / no): yes
enter the quantity : 1
enter the amount : 50
do you want to add more items (yes / no): no
----------------------------------------
name : Rahul
product : Groceries
Amount to be paid : 250
----------------------------------------
*************HAPPY CUSTOMER*************
```

---

## ⚠️ Notes

* No input validation included
* Quantity and amount must be numeric values
* Runs in terminal/command prompt only

---

## 🚀 Future Improvements

* Add item-wise list display
* Add GST/tax calculation
* Save bill to file
* GUI version (Tkinter/Web)

---

## 📄 License

Free to use for learning purposes.
