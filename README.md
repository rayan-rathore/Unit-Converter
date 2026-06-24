# Unit Converter (Python CLI)

A command-line **unit conversion application** built in Python using an object-oriented design.
It allows users to convert values across multiple categories such as **length, weight, volume, time, digital data, area, speed, energy, power, and pressure**.

This project was built as a structured Python practice project with a focus on:

* **Object-oriented programming**
* **Input validation**
* **Separation of concerns**
* **Modular project structure**
* **Reusable conversion logic**

---

## Features

* Convert values across **10 unit categories**
* Supports **multiple units per category**
* **Input validation** for categories, units, and numeric values
* **Loop-based CLI interface** for repeated conversions
* Organized into separate modules for:

  * conversion logic
  * category handling
  * unit data
  * user interaction

---

## Supported Categories

The converter currently supports the following categories:

* **Length**
* **Weight / Mass**
* **Volume**
* **Time**
* **Digital Data**
* **Area**
* **Speed**
* **Energy**
* **Power**
* **Pressure**

---

## Supported Units

### 1) Length

* nanometer
* micrometer
* millimeter
* centimeter
* decimeter
* meter
* kilometer
* inch
* foot
* yard
* mile
* nautical_mile

### 2) Weight / Mass

* microgram
* milligram
* gram
* kilogram
* stone
* pound
* ounce
* ton_metric
* ton_short
* ton_long

### 3) Volume

* milliliter
* cubic_centimeter
* liter
* cubic_meter
* cup_us
* pint_us
* quart_us
* gallon_us
* fluid_ounce_us
* tablespoon_us
* teaspoon_us
* cup_uk
* pint_uk
* quart_uk
* gallon_uk
* fluid_ounce_uk

### 4) Time

* nanosecond
* microsecond
* millisecond
* second
* minute
* hour
* day
* week
* month_average
* year_standard
* year_leap
* decade
* century

### 5) Digital Data

* bit
* nibble
* byte
* kilobyte
* megabyte
* gigabyte
* terabyte
* petabyte

### 6) Area

* square_millimeter
* square_centimeter
* square_meter
* square_kilometer
* square_inch
* square_foot
* square_yard
* square_mile
* acre
* hectare

### 7) Speed

* meters_per_second
* kilometers_per_hour
* miles_per_hour
* knot
* mach

### 8) Energy

* joule
* kilojoule
* gram_calorie
* kilocalorie
* watt_hour
* kilowatt_hour
* british_thermal_unit
* electronvolt

### 9) Power

* milliwatt
* watt
* kilowatt
* megawatt
* gigawatt
* horsepower_mechanical
* horsepower_metric

### 10) Pressure

* pascal
* kilopascal
* bar
* atmosphere
* torr
* psi

---

# Project Structure

```bash
unit-converter/
│
├── main.py                # CLI / user interaction
├── conversionengine.py    # Conversion engine logic
├── categories.py         # StandardCategory class
├── data.py               # UNIT_DATA dictionary
└── README.md
```

---

## How It Works

The project uses a **base-unit conversion approach**.

Each category has:

* a **base unit**
* a dictionary of supported units and their multiplier relative to that base unit

### Example

For the **length** category:

* base unit = `meter`
* `kilometer = 1000.0`
* `centimeter = 0.01`
* `inch = 0.0254`

To convert from one unit to another, the program uses this formula:

```python
final_value = from_multiplier * value / to_multiplier
```

### Conversion flow

For example, converting **5 kilometers to meters**:

1. Get multiplier for `kilometer`
2. Get multiplier for `meter`
3. Apply formula
4. Return converted result

This works well for **linear unit conversions** where all units can be represented relative to a single base unit.

---

# Object-Oriented Design

The project is split into two main classes:

## 1. `StandardCategory`

Represents a single conversion category such as `length`, `volume`, or `time`.

### Responsibilities

* Store category metadata
* Store units and multipliers
* Perform conversion calculations
* Return available units in that category

### Main methods

* `calculation(from_unit, to_unit, value)`
* `available_units()`

---

## 2. `ConversionEngine`

Acts as the controller for the application.

### Responsibilities

* Load all categories from `UNIT_DATA`
* Store category objects
* Validate categories and units
* Execute conversions by delegating to the correct category object

### Main methods

* `setup_categories()`
* `get_categories_name()`
* `is_valid_category()`
* `get_categories_units()`
* `is_valid_units()`
* `execute_conversion()`

---

# Example Usage

```text
----Welcome to Unit converter!----

Available categories : ['length', 'weight_mass', 'volume', 'time', 'digital_data', 'area', 'speed', 'energy', 'power', 'pressure']

What do you want to convert? please select from above list.
length

Available Units : ['nanometer', 'micrometer', 'millimeter', 'centimeter', 'decimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile', 'nautical_mile']

Please select unit from which you want to convert.
meter

What is the value of your chosen unit?
1500

To which unit you want to convert that value?
kilometer

1500.0 Meter is equal to 1.500 Kilometer.
Would you like another conversion? (y/n)
```

---

# Input Validation

The application includes validation for:

## Category validation

If the user enters an invalid category, the program asks again until a valid category is provided.

## Unit validation

If the user enters a unit that does not belong to the selected category, the program asks again.

## Numeric validation

If the entered value cannot be converted to a number, the program catches the error and asks for a valid numeric input.

This makes the CLI more user-friendly and prevents the program from crashing on bad input.

---

# Why Temperature Is Not Included

Temperature conversion is intentionally **not included in this project**.

This converter is built around **multiplier-based unit conversion**, where every unit in a category can be expressed relative to a single base unit.

That works for categories like:

* length
* weight
* volume
* speed
* energy
* pressure

However, **temperature conversion is different** because it requires **offset-based formulas**, not just multiplication.

For example:

* Celsius to Fahrenheit
* Fahrenheit to Celsius
* Celsius to Kelvin

These conversions involve addition/subtraction as well as multiplication, so they do not fit cleanly into the current architecture.

Because of that, temperature was kept as a **separate program** instead of forcing special-case logic into this project.

---

# Design Decisions

## 1. Separate modules

The project is split into multiple files so that each file has a clear responsibility:

* `data.py` stores raw conversion data
* `categories.py` handles category-level conversion logic
* `conversionengine.py` manages the conversion system
* `main.py` handles user interaction

This keeps the code easier to read, maintain, and extend.

---

## 2. Base-unit conversion model

Instead of writing separate formulas for every possible unit pair, the project stores all units relative to a **base unit** and uses one common formula for conversion.

This reduces repetition and makes it easy to add new units.

---

## 3. Reusable category class

A single `StandardCategory` class is used for all categories that follow multiplier-based conversion logic.

This avoids duplicating conversion code for every category.

---

## 4. Repeated conversion loop

The CLI allows users to perform multiple conversions in one run without restarting the program.

---

# Limitations

## 1. Only supports multiplier-based conversions

The current design does **not** support categories that require custom formulas, such as temperature.

## 2. CLI-only interface

The application currently runs only in the terminal and does not include a graphical interface.

## 3. No unit aliases

The user must enter the unit names exactly as defined in the program data.

For example:

* `kilometer`
* `square_meter`
* `fluid_ounce_us`

Aliases like `km`, `m`, `kg`, etc. are not currently supported.

---

# Possible Future Improvements

Here are some improvements that could be added in future versions:

## Usability Improvements

* Support unit aliases like `km`, `kg`, `m`, `ft`, `lb`
* Replace underscores with user-friendly labels in CLI output
* Add category numbering/menu selection
* Improve formatting of displayed unit names
* Allow direct quit commands like `q` or `exit`

---

# Learning Goals of This Project

This project was built to practice and reinforce:

* Python classes and objects
* modular programming
* dictionaries and nested data structures
* validation logic
* loops and exception handling
* separating business logic from user interaction
* designing a reusable conversion system

---

