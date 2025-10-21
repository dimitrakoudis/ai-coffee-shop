import os

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
MENU_SERVICE_BASE_URL = os.getenv(
    "MENU_SERVICE_BASE_URL",
    "https://raw.githubusercontent.com/dimitrakoudis/"
    "ai-coffee-shop/refs/heads/main/menu_service",
)
