import requests

def register():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    data = {
        "name": "Goutam Aswani",
        "regNo": "0827AL221053",
        "email": "goutamaswani221152@acropolis.in"
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Webhook generated successfully.")
        result = response.json()
        return result["webhook"], result["accessToken"]
    else:
        print("Registration failed with status:", response.status_code)
        print(response.text)
        return None, None
    
    
def get_query():
    query = """
    SELECT
        p.AMOUNT AS SALARY,
        CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
        TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
        d.DEPARTMENT_NAME
    FROM PAYMENTS p
    JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
    WHERE DAY(p.PAYMENT_TIME) != 1
    ORDER BY p.AMOUNT DESC
    LIMIT 1;
    """
    return query.strip()
token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdBTDIyMTA1MyIsIm5hbWUiOiJHb3V0YW0gQXN3YW5pIiwiZW1haWwiOiJnb3V0YW1hc3dhbmkyMjExNTJAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYxMjY0LCJleHAiOjE3NDY5NjIxNjR9.pAyh3YqX3v2YRL2QZZ5-TdWQpZ4YNI2XQhqlzLaNNPg"
def submit(webhook, token, query):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "finalQuery": query
    }

    response = requests.post(webhook, headers=headers, json=data)
    if response.status_code == 200:
        print("Query submitted successfully.")
    else:
        print("Submission failed with status:", response.status_code)
        print(response.text)

def main():
    webhook, token = register()
    if webhook is not None and token is not None:
        query = get_query()
        submit(webhook, token, query)
    else:
        print("Could not proceed due to registration error.")

main()
