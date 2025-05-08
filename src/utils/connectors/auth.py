from utils.auxiliary.queries import get_with_retries
from utils.connectors.app_urls import WOODMAC_LDI_ENDPOINT

def authenticate_user(username, password):
    data = get_with_retries(WOODMAC_LDI_ENDPOINT, username, password)

    # If the response contains an error message
    if "error" in data:
        return {"status_code": 401, "error": data["error"]}
    
    # Successful authentication
    return {"status_code": 200, "data": data}
