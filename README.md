# 🎯 COCOHelper Library

> A simple and powerful Python library for working with **COCO / YOLO classes** in an organized and beginner-friendly way.

---

## 🌟 Overview

`COCOHelper` is a lightweight helper class that provides categorized access to **COCO dataset classes**, allowing you to:
- Get class names or IDs by category (e.g., animals, electronics, etc.)
- Display all available categories and details
- Use clean, human-readable methods — perfect for YOLO users and dataset visualization projects.

---

## 🚀 Installation

You can install it directly via `pip` (after publishing to PyPI):

```bash
pip install cocohelper
````

Or locally (if you have the code):

```bash
pip install .
```

---

## 💡 Usage Example

```python
from cocohelper import COCOHelper

# Initialize
coco = COCOHelper()

# Get all classes in a category
print(coco.get_classes("animals"))

# Get all IDs in multiple categories
print(coco.get_ids("transport", "electronics"))

# Show all category names
coco.show_all_categories()

# Show all details (IDs + class names)
coco.show_all_details()
```

---

## 🧩 Available Methods

| Method                     | Description                                          |
| :------------------------- | :--------------------------------------------------- |
| `get_ids(*categories)`     | Returns a list of class IDs for given categories     |
| `get_classes(*categories)` | Returns a list of class names for given categories   |
| `show_all_categories()`    | Prints all available COCO categories                 |
| `show_all_details()`       | Prints all categories with their class names and IDs |
| `help()`                   | Displays usage help                                  |

---

## 📚 Example Output

```text
========================================
📘 AVAILABLE CATEGORIES
========================================
01. Person
02. transport
03. traffic & signs
04. animals
05. personal items
06. sports & recreation
07. food & kitchen
08. indoor objects
09. electronics
10. appliances
11. miscellaneous
```

---

## 🧠 Why Use COCOHelper?

✅ Simple & ready to use
✅ Clean, readable structure
✅ Perfect for YOLO / COCO experiments
✅ Helps organize custom datasets easily

---

## 🧑‍💻 Author

**Ahmad Ashraf**
📧 [ahmadashrafglal@gmail.com](mailto:ahmadashrafglal@gmail.com)
💼 [LinkedIn](https://www.linkedin.com/in/ahmadashrafgalal)

---

## ⚙️ Version Info

| Version |    Date    | Notes           |
| :-----: | :--------: | :-------------- |
|  1.0.0  | 2025-10-18 | Initial release |

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.

---

>  *“COCOHelper — making object detection classes simple, structured, and fun!”*
