# collectionManipulator# Student Data Organizer (Collection Manipulator)

A clean, menu-driven Python application designed to manage student records efficiently while demonstrating the practical application of core data types and memory concepts.

---

## 🚀 Key Features & Implementation Details

Instead of generic variables, this project utilizes specialized Python collection types based on their technical properties:

* **List (`records`)**: Used as an ordered, mutable sequence to hold all student dictionaries, enabling smooth iteration and display.
* **Dictionary (`db`)**: Implemented for $O(1)$ fast lookups where the unique `Student ID` acts as the key for instant data retrieval.
* **Tuple (`fixed_data`)**: Used specifically for `Student ID` and `Date of Birth`. Since tuples are **immutable**, this guarantees that core identity data cannot be accidentally modified after creation.
* **Set (`all_subjects` & `sub_set`)**: Leveraged for managing subjects. It automatically eliminates duplicate entries and handles unique course rosters effortlessly.

---

## 🛠️ Concepts Demonstrated

1.  **Data Type Casting**: Explicitly converting user inputs using `int()` for IDs and Ages to prevent structural errors.
2.  **String Manipulation**: Using `.split()` and `.strip()` via comprehension to clean up comma-separated user inputs seamlessly.
3.  **Dynamic Memory Management**: Utilizing Python's native `del` keyword to permanently purge records from the database dictionary during deletion.
4.  **Modern Formatting**: Employing Python f-strings for clean, readable console outputs.

---

## 🖥️ How to Run

1. Open your terminal or command prompt.
2. Run the script using:
   ```bash
   python main.py
