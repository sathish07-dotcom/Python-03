# 🌀 Loops in Python

Loops in Python are used to execute a block of code repeatedly as long as a certain condition is met or for a set number of times. Python supports two main types of loops:

## 🔁 1. `for` Loop

The `for` loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

### **Syntax**:
```python
for item in iterable:
    # do something
```

### **Example**:
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

### **With `range()`**:
```python
for i in range(5):
    print(i)  # prints 0 to 4
```

---

## 🔁 2. `while` Loop

The `while` loop runs as long as a given condition is `True`.

### **Syntax**:
```python
while condition:
    # do something
```

### **Example**:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 🔄 Loop Control Statements

Python provides control statements to manage the flow of loops:

- **`break`** – exits the loop prematurely
- **`continue`** – skips the current iteration and continues with the next
- **`pass`** – does nothing, acts as a placeholder

### **Examples**:
```python
for i in range(10):
    if i == 5:
        break  # loop stops when i is 5
    print(i)
```

```python
for i in range(5):
    if i == 2:
        continue  # skips the iteration when i is 2
    print(i)
```

---

## ✅ Tips

- Avoid infinite loops by ensuring conditions eventually become `False`.
- Use `else` with loops to run a block of code after the loop finishes normally (without `break`).

```python
for i in range(3):
    print(i)
else:
