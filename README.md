# 🔄 TransQueue
```
<!-- ············································································································ -->
<!-- :   ███████████                                           ██████                                           : -->
<!-- :  ░█░░░███░░░█                                         ███░░░░███                                         : -->
<!-- :  ░   ░███  ░  ████████   ██████   ████████    █████  ███    ░░███ █████ ████  ██████  █████ ████  ██████ : -->
<!-- :      ░███    ░░███░░███ ░░░░░███ ░░███░░███  ███░░  ░███     ░███░░███ ░███  ███░░███░░███ ░███  ███░░███: -->
<!-- :      ░███     ░███ ░░░   ███████  ░███ ░███ ░░█████ ░███   ██░███ ░███ ░███ ░███████  ░███ ░███ ░███████ : -->
<!-- :      ░███     ░███      ███░░███  ░███ ░███  ░░░░███░░███ ░░████  ░███ ░███ ░███░░░   ░███ ░███ ░███░░░  : -->
<!-- :      █████    █████    ░░████████ ████ █████ ██████  ░░░██████░██ ░░████████░░██████  ░░████████░░██████ : -->
<!-- :     ░░░░░    ░░░░░      ░░░░░░░░ ░░░░ ░░░░░ ░░░░░░     ░░░░░░ ░░   ░░░░░░░░  ░░░░░░    ░░░░░░░░  ░░░░░░  : -->
<!-- ············································································································ -->
```
## 🚀 Key Features

✅ RESTful API to receive user transactions  
✅ Unique transaction ID generation (timestamp + random)  
✅ MongoDB-based transaction queue (Collection: `Q`)  
✅ Background transaction processor using `multiprocessing`  
✅ Easy to integrate and extend via `transaction_module`

---
## ⚙️ Tech Stack

- 🐍 Python 3.x  
- 🔥 Flask  
- 🧠 PyMongo  
- ⚙️ multiprocessing  
- 🛢️ MongoDB  
---
## 📬 API Endpoint

### `POST /api/data/`

Submits a transaction to the queue.

**Request JSON:**
```
{
  "username": "user123",
  "value": 150.0
}
```
Success Response:
{
  "status": "success",
  "message": "Data received for user user123",
  "data": {
    "username": "user123",
    "value": 150.0,
    "transaction_id": "172312840112395849234"
  }
}
---
Error Response (Invalid Input):
```
{
  "status": "error",
  "message": "Invalid input. You must provide a username and a numeric value."
}
```
