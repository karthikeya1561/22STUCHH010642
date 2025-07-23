// Defining the params here
type params = {
  stack: string;
  level: string;
  pkg: string;
  message: string;
};

// Function to log the message
const TESTAPISERVER = "http://20.244.56.144/evaluation-service/register";
const token =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJrb25kdXJpc3VyeWFrYXJ0aGlrZXlhMjJAaWZoZWluZGlhLm9yZyIsImV4cCI6MTc1MzI1MjY2NiwiaWF0IjoxNzUzMjUxNzY2LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiOTM2MTk3NGYtMGQ4NS00NzgzLWEzNjEtNjMyMjM3MzAxZGMyIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiayBzdXJ5YSBrYXJ0aGlrZXlhIiwic3ViIjoiOTVlOTliYWQtYjk5NS00YWNhLWI5MjktMDM3MjczNjJmOWU5In0sImVtYWlsIjoia29uZHVyaXN1cnlha2FydGhpa2V5YTIyQGlmaGVpbmRpYS5vcmciLCJuYW1lIjoiayBzdXJ5YSBrYXJ0aGlrZXlhIiwicm9sbE5vIjoiMjJzdHVjaGgwMTA2NDIiLCJhY2Nlc3NDb2RlIjoiYkN1Q0ZUIiwiY2xpZW50SUQiOiI5NWU5OWJhZC1iOTk1LTRhY2EtYjkyOS0wMzcyNzM2MmY5ZTkiLCJjbGllbnRTZWNyZXQiOiJ1c1RUTmZKY3RHa3VVQkFSIn0.7jX43ccUnTuEdyEh-Md9B6O2K99Zp3ChRPZ3xWTgEl8";

export const log = async (params: params) => {
  const { stack, level, pkg, message } = params;

  // Constructing the payload
  const payload = {
    stack,
    level,
    package: pkg,
    message,
  };

  // Sending the POST request
  try {
    const response = await fetch(TESTAPISERVER, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error logging message:", error);
  }
};
