#pip install request
import requests

target_url = "http://notexisting.com"
#target_url = "http://www.google.com"

try:
    # Simuleer een aanvraag met een netwerkbibliotheek
    response = requests.get(target_url, timeout=5) # Kan een fout veroorzaken
    print("Request successful!")
except requests.ConnectionError:
    print("Failed to connect to the target")
except requests.Timeout:
    print("Request timed out")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
