from utils.auxiliary.queries import get_with_retries
from utils.connectors.app_urls import WOODMAC_FIELD_MONTHLY_PRODUCTION

def fetch_production_data(username, password):
    response = get_with_retries(WOODMAC_FIELD_MONTHLY_PRODUCTION, username, password)
    return response.get("value", []) if response else []

