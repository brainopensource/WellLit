import requests
from requests.auth import HTTPBasicAuth
import time


def get_with_retries(url, username, password, max_retries=2, timeout=30, delay=5):
    """
    Attempts to perform a GET request with basic authentication up to 'max_retries' times.
    Returns the JSON response if status_code is 200.
    Otherwise, returns an error message.
    """
    response = None
    for attempt in range(1, max_retries + 1):
        try:
            print('\n Trying to connect to Woodmac...', url, username)
            response = requests.get(
                url,
                auth=HTTPBasicAuth(username, password),
                timeout=timeout,
                headers={"Accept": "application/json"},
            )
            print(response, response.status_code, response.text)

            # Check if the response status code is 200
            if response.status_code == 200:
                return response.json()
            else:
                delay = delay + attempt * 3
                timeout = timeout + attempt * 15
                print(f"[Attempt {attempt}] Status: {response.status_code} - Retrying in {delay}s...")
                print("\n Delay", delay, "Timeout", timeout)
                time.sleep(delay)

        except Exception as e:
            print(f"[Attempt {attempt}] Exception: {e} - Retrying in {delay}s...")
            time.sleep(delay)

    # If all attempts failed, return a structured error message
    if response:
        return {"error": f"Request failed with status code {response.status_code}: {response.text}"}
    else:
        return {"error": "No response received after multiple attempts."}
