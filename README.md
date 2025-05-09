# 🛒 BestBuy - Command-Line Store OOP System

A modular and object-oriented command-line shopping system written in Python.  
This project demonstrates clean separation of concerns, good OOP practices, and CSV-based state handling.  
Users can browse products, make orders, manage a shopping cart, and exit safely — all via a simple CLI.

---

## 📁 Project Structure

```bash
    bestBuy/
        │
        ├── main.py # Entry point with CLI menu
        ├── store.py # Store class managing products
        ├── products.py # Product class with quantity handling
        │
        ├── data_manager/
        │     └── load_cart.py # Cart functions: add, delete, show, restore
        │
        ├── data/
        │     └── basket.csv # Generated shopping cart (temporary)
        │
        ├── requirements.txt # Project dependencies
        └── README.md # This file
```

---

## 🚀 Features

- Object-Oriented structure (Store, Product classes)
- View all products in the store
- View total quantity in store
- Add items to shopping cart
- Save shopping cart to a CSV file
- View and delete shopping cart
- Restore deleted cart items back to stock
- Exit cleanly with automatic cart deletion

---

## ▶️ How to Run

```bash
  python main.py
```

---

## 🧪 Requirements

Python 3.8+
(Standard library only – no external dependencies required)

---

## 📌 Notes

- The shopping cart is stored in data/basket.csv
- On exit, the cart is automatically deleted
- If cart is deleted manually, products are restored to inventory

---

## 💡 Future Improvements

- Add file-based persistence for product inventory
- Implement product search or filtering
- Add unit tests and logging

---