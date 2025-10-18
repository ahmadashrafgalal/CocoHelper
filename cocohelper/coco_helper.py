"""
🎯 COCOHelper Library
---------------------
A simple and powerful helper for working with YOLO / COCO classes.

Author: Ahmad Ashraf
Version: 1.0
Date: 2025-10-18

Usage:
    from cocohelper import get_classes, get_ids, show_all_categories

    print(get_classes("animals"))
    print(get_ids("transport"))
    show_all_categories()
"""

class _COCOHelper:
    """Internal class — handles all COCO categories and logic."""

    def __init__(self):
        self.categories = {
            "Person": {
                0: "person"
            },
            "transport": {
                1: "bicycle",
                2: "car",
                3: "motorcycle",
                4: "airplane",
                5: "bus",
                6: "train",
                7: "truck",
                8: "boat"
            },
            "traffic & signs": {
                9: "traffic light",
                10: "fire hydrant",
                11: "stop sign",
                12: "parking meter",
                13: "bench"
            },
            "animals": {
                14: "bird",
                15: "cat",
                16: "dog",
                17: "horse",
                18: "sheep",
                19: "cow",
                20: "elephant",
                21: "bear",
                22: "zebra",
                23: "giraffe"
            },
            "personal items": {
                24: "backpack",
                25: "umbrella",
                26: "handbag",
                27: "tie",
                28: "suitcase"
            },
            "sports & recreation": {
                29: "frisbee",
                30: "skis",
                31: "snowboard",
                32: "sports ball",
                33: "kite",
                34: "baseball bat",
                35: "baseball glove",
                36: "skateboard",
                37: "surfboard",
                38: "tennis racket"
            },
            "food & kitchen": {
                39: "bottle",
                40: "wine glass",
                41: "cup",
                42: "fork",
                43: "knife",
                44: "spoon",
                45: "bowl",
                46: "banana",
                47: "apple",
                48: "sandwich",
                49: "orange",
                50: "broccoli",
                51: "carrot",
                52: "hot dog",
                53: "pizza",
                54: "donut",
                55: "cake"
            },
            "indoor objects": {
                56: "chair",
                57: "couch",
                58: "potted plant",
                59: "bed",
                60: "dining table",
                61: "toilet"
            },
            "electronics": {
                62: "tv",
                63: "laptop",
                64: "mouse",
                65: "remote",
                66: "keyboard",
                67: "cell phone"
            },
            "appliances": {
                68: "microwave",
                69: "oven",
                70: "toaster",
                71: "sink",
                72: "refrigerator"
            },
            "miscellaneous": {
                73: "book",
                74: "clock",
                75: "vase",
                76: "scissors",
                77: "teddy bear",
                78: "hair drier",
                79: "toothbrush"
            }
        }

    def get_ids(self, *category_names):
        ids = []
        for name in category_names:
            if name in self.categories:
                ids.extend(list(self.categories[name].keys()))
            else:
                print(f"⚠️ Category '{name}' not found!")
        return ids

    def get_classes(self, *category_names):
        names = []
        for name in category_names:
            if name in self.categories:
                names.extend(list(self.categories[name].values()))
            else:
                print(f"⚠️ Category '{name}' not found!")
        return names

    def show_all_categories(self):
        print("\n" + "=" * 40)
        print("📘 AVAILABLE CATEGORIES")
        print("=" * 40)
        for i, category in enumerate(self.categories.keys(), start=1):
            print(f"{i:02d}. {category}")

    def show_all_details(self):
        print("\n" + "=" * 50)
        print("📘 CATEGORIES & CLASSES DETAILS")
        print("=" * 50)
        for category, items in self.categories.items():
            print(f"\n🔹 {category.upper()}")
            print("-" * (len(category) + 6))
            for cls_id, cls_name in items.items():
                print(f"   • ID {cls_id:>2}: {cls_name}")


# =========================
# Public interface (clean API)
# =========================
__all__ = ["get_ids", "get_classes", "show_all_categories", "show_all_details", "help"]

# internal instance (used by wrappers)
_coco = _COCOHelper()

def get_ids(*args):
    """📊 Return class IDs for given categories."""
    return _coco.get_ids(*args)

def get_classes(*args):
    """🏷️ Return class names for given categories."""
    return _coco.get_classes(*args)

def show_all_categories():
    """📚 Print all category names."""
    return _coco.show_all_categories()

def show_all_details():
    """📚 Print all categories and classes."""
    return _coco.show_all_details()

def help():
    """🆘 Display all available methods."""
    print("""
Available Methods:
------------------
✅ get_ids(*categories)        → Returns list of class IDs.
✅ get_classes(*categories)    → Returns list of class names.
✅ show_all_categories()       → Prints all COCO categories.
✅ show_all_details()          → Prints categories and classes.
✅ help()                      → Shows this help message.
""")
