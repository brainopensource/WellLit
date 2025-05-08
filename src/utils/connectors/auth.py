from utils.auxiliary.queries import get_with_retries
from utils.connectors.app_urls import WOODMAC_LDI_ENDPOINT

def authenticate_user(username, password):
    params = {
        "$top": "1", "$select": "reference_period",}

    data = get_with_retries(WOODMAC_LDI_ENDPOINT, username, password, params)

    # If the response contains an error message
    if "error" in data:
        return {"status_code": 401, "error": data["error"]}
    
    # Successful authentication
    return {"status_code": 200, "data": data}
