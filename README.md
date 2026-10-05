# 🍽️ Restaurant Management — Python OOP

A command-line **restaurant management system built with Python**, designed to practice Object-Oriented Programming (OOP) concepts.

## 📖 About the Project

This project is a terminal-based restaurant management application that allows users to register, remove, list, and update restaurants.

It also includes a basic **restaurant assessment system**, allowing users to assign grades from 1 to 10.

The project was developed as a practical exercise to strengthen Python and Object-Oriented Programming skills.

## ✨ Features

- Add restaurants
- Remove restaurants
- List registered restaurants
- Update restaurant information
  - Name
  - Category
  - Status
- Restaurant status indicator
- Add restaurant assessments
- Assign grades from 1 to 10
- Interactive command-line menus
- Basic input validation

The main menu provides access to restaurant management and the assessment system.

## 🛠️ Technologies

- **Python 3**
- Object-Oriented Programming
- Command Line Interface (CLI)

## 📚 OOP Concepts Practiced

This project explores several Python OOP concepts:

- Classes and objects
- Constructors (`__init__`)
- Class attributes
- Instance attributes
- `@classmethod`
- `@staticmethod`
- `@property`
- Special methods (`__repr__`)
- Object relationships
- Lists of objects

The `Restaurant` class manages the restaurant data, while assessments are represented through the `Assessment` class.

## ⭐ Assessment System

Restaurants can receive grades from **1 to 10**.

The assessment functionality allows the user to select a restaurant by its ID and assign a grade, which is stored in the restaurant's assessment list.

## 📂 Project Structure

```text
Restaurant-Management-OO-Python/
│
└── OO Python/
    ├── app.py
    └── models/
        └── assessment.py
        └── restaurant.py
```

### `app.py`

Application entry point responsible for starting the restaurant management menu.

### `restaurant.py`

Contains the `Restaurant` class and the main application logic, including restaurant registration, removal, listing, updating, and assessments.

### `assessment.py`

Contains the `Assessment` class, which represents an assessment with a client and a grade.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/EduPanage/Restaurant-Management-OO-Python.git
```

### 2. Navigate to the project directory

```bash
cd Restaurant-Management-OO-Python/"OO Python"
```

### 3. Run the application

```bash
python app.py
```

## 🎯 Purpose

The main goal of this project is to practice **Object-Oriented Programming with Python** through the development of a small, interactive application.

It focuses on applying OOP concepts to a practical scenario while progressively adding features such as CRUD operations and restaurant assessments.

## 👨‍💻 Author

**Eduardo Panage**

[GitHub](https://github.com/EduPanage)

## 📄 License

This project was developed for educational and programming practice purposes.
