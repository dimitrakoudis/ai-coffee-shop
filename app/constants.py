import os

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
MAIN_WAITER_NAME = os.getenv("MAIN_WAITER_NAME", "John Doe")
MENU_SERVICE_BASE_URL = os.getenv(
    "MENU_SERVICE_BASE_URL",
    "https://raw.githubusercontent.com/dimitrakoudis/"
    "ai-coffee-shop/refs/heads/main/menu_service",
)
