import requests

TESTAPISERVER = "http://20.244.56.144/evaluation-service/register"
token = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJrb25kdXJpc3VyeWFrYXJ0aGlrZXlhMjJAaWZoZWluZGlhLm9yZyIsImV4cCI6MTc1MzI1MjY2NiwiaWF0IjoxNzUzMjUxNzY2LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiOTM2MTk3NGYtMGQ4NS00NzgzLWEzNjEtNjMyMjM3MzAxZGMyIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiayBzdXJ5YSBrYXJ0aGlrZXlhIiwic3ViIjoiOTVlOTliYWQtYjk5NS00YWNhLWI5MjktMDM3MjczNjJmOWU5In0sImVtYWlsIjoia29uZHVyaXN1cnlha2FydGhpa2V5YTIyQGlmaGVpbmRpYS5vcmciLCJuYW1lIjoiayBzdXJ5YSBrYXJ0aGlrZXlhIiwicm9sbE5vIjoiMjJzdHVjaGgwMTA2NDIiLCJhY2Nlc3NDb2RlIjoiYkN1Q0ZUIiwiY2xpZW50SUQiOiI5NWU5OWJhZC1iOTk1LTRhY2EtYjkyOS0wMzcyNzM2MmY5ZTkiLCJjbGllbnRTZWNyZXQiOiJ1c1RUTmZKY3RHa3VVQkFSIn0.7jX43ccUnTuEdyEh-Md9B6O2K99Zp3ChRPZ3xWTgEl8"
)

def log(stack: str, level: str, pkg: str, message: str):
    payload = {
        "stack": stack,
        "level": level,
        "package": pkg,
        "message": message,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.post(TESTAPISERVER, json=payload, headers=headers)
        response.raise_for_status()
    except requests.RequestException as error:
        print("Error logging message:", error)