Here are the commands to interact with a `Serializer` for fetching, creating, updating, and listing data, using **Django REST Framework serializers**. 

---

### **1. Get a Single Object**
```python
# Example data (a single object fetched from a database)
student = {"id": 1, "name": "John", "roll": 12, "city": "Lahore"}

# Serialize the object
serializer = StudentSerializer(student)
print(serializer.data)  # Output: {"id": 1, "name": "John", "roll": 12, "city": "Lahore"}
```

---

### **2. Get a List of Objects**
```python
# Example data (a list of objects fetched from a database)
students = [
    {"id": 1, "name": "John", "roll": 12, "city": "Lahore"},
    {"id": 2, "name": "Jane", "roll": 15, "city": "Karachi"}
]

# Serialize the list of objects
serializer = StudentSerializer(students, many=True)
print(serializer.data)
# Output: [{"id": 1, "name": "John", "roll": 12, "city": "Lahore"}, {"id": 2, "name": "Jane", "roll": 15, "city": "Karachi"}]
```

---

### **3. Create an Object**
```python
# Example input data
input_data = {"id": 3, "name": "Alice", "roll": 18, "city": "Islamabad"}

# Deserialize and validate
serializer = StudentSerializer(data=input_data)
if serializer.is_valid():
    validated_data = serializer.validated_data
    print(validated_data)  # Output: {"id": 3, "name": "Alice", "roll": 18, "city": "Islamabad"}
else:
    print(serializer.errors)  # Handle validation errors
```

---

### **4. Update an Existing Object**
```python
# Existing object data (e.g., fetched from a database)
existing_student = {"id": 1, "name": "John", "roll": 12, "city": "Lahore"}

# Updated data
updated_data = {"id": 1, "name": "John Updated", "roll": 20, "city": "Lahore Updated"}

# Deserialize with partial=True for partial updates
serializer = StudentSerializer(existing_student, data=updated_data)
if serializer.is_valid():
    updated_student = serializer.validated_data
    print(updated_student)
    # Output: {"id": 1, "name": "John Updated", "roll": 20, "city": "Lahore Updated"}
else:
    print(serializer.errors)  # Handle validation errors
```

---

### **5. Partial Update (PATCH)**
```python
# Existing object data (e.g., fetched from a database)
existing_student = {"id": 1, "name": "John", "roll": 12, "city": "Lahore"}

# Partial update data
partial_data = {"roll": 25}

# Deserialize with partial=True for partial updates
serializer = StudentSerializer(existing_student, data=partial_data, partial=True)
if serializer.is_valid():
    updated_student = serializer.validated_data
    print(updated_student)
    # Output: {"id": 1, "name": "John", "roll": 25, "city": "Lahore"}
else:
    print(serializer.errors)  # Handle validation errors
```

---

### **6. Delete (Simulated)**
Note: Deletion doesn’t involve a serializer directly unless you use it for validation. Just use your database command to delete an object.

```python
# Assume the object is deleted from the database
print("Object deleted successfully.")  # Simulate deletion
```

---

These commands cover fetching single or multiple objects, creating, updating, and handling partial updates using DRF serializers. Adjust the `data` and `existing_student` as needed for your specific use case.