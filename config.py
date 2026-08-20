import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = "https://the-internet.herokuapp.com"
BROWSER = "chromium"
HEADLESS = True
SLOW_MO = 500

# Credentials
BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME", "")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "")