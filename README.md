# 🎯 COCOHelper Library

> A simple and powerful Python library for working with **COCO / YOLO classes** in an organized and beginner-friendly way.

---

## 🌟 Overview

`COCOHelper` is a lightweight utility that provides **categorized access to COCO dataset classes**, allowing you to:

- Get class names or IDs by category (e.g., animals, electronics, etc.)
- Display all available categories and details
- Use a clean, human-readable API — perfect for YOLO users and dataset visualization projects.

---

## 🚀 Installation

You can install it directly via **pip** (after publishing to PyPI):

```bash
pip install cocohelper
````

Or install it locally (if you have the source code):

```bash
pip install .
```

---

## 💡 Usage Example

```python
from cocohelper import get_classes, get_ids, show_all_categories, show_all_details

# Get all class names in a category
print(get_classes("animals"))

# Get class IDs in multiple categories
print(get_ids("transport", "electronics"))

# Show all available category names
show_all_categories()

# Show detailed list of categories, IDs, and class names
show_all_details()
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
✅ Clean, beginner-friendly API
✅ Ideal for YOLO / COCO projects
✅ Helps organize and visualize datasets easily
✅ Designed for quick access to class names and IDs

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

> *“COCOHelper — making object detection classes simple, structured, and fun!”*
