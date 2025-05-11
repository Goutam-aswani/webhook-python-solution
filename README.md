# webhook-python-solution
Build a Python application that: • On startup, send a POST request to generate a webhook. • Based on the response, solve a SQL problem and store the result. • Send the solution (a final SQL query) to the returned webhook URL using the authentication token received.

# Webhook SQL Submission – Bajaj Hiring Challenge

This project is a Python application that automatically:
- Sends a POST request to generate a webhook and token
- Solves a SQL query problem based on the regNo
- Submits the SQL solution to the webhook using the given token

---

## 🔧 Technologies Used

- Python 3
- Requests library (for API calls)
- SQL (for query formulation)

---
## ▶️ How to Run

1. Clone the repository:

git clone https://github.com/your-username/webhook-sql-solution.git
cd webhook-sql-solution
pip install -r requirements.txt
python postrequest.py

