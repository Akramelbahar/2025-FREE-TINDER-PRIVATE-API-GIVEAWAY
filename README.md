# TINDER-ANDROID-API-WITH-REFRESH-TOKEN-EXTRACT-METHOD
This repository contains a Python-based API for interacting with Tinder, enabling profile scraping, authentication management, and customization of preferences. The code integrates with Tinder's backend through Protobuf decoding and HTTP requests.
# Tinder Scraper API

This repository provides a Python-based Tinder API wrapper to automate profile scraping, token management, and preferences customization. It uses Protobuf decoding and HTTP requests to interact with Tinder's backend.

## Key Features  
- **Authentication Management**: Generate or refresh authentication tokens using Protobuf communication.  
- **Profile Search**: Fetch Tinder recommendations programmatically.  
- **Location Updates**: Update the Tinder location using latitude and longitude.  
- **Preferences Customization**: Change age range, distance filters, and gender preferences.  
- **Proxy Support**: Integrate proxies for IP rotation.  

## Requirements  
- Python 3.x  
- Install required libraries:  
  `pip install requests protobuf random protobuf-decoder`  

## Environment Setup  
1. **Rooted Android Emulator (MEmu):** Install and configure MEmu. Enable root access under `Settings > Developer Options`.  
2. **Install Frida Tools:** Install Frida on your system: `pip install frida-tools`  
3. **Attach Frida to Tinder:** Prepare your Frida script (`tinder_scraper.js`). Run: `frida -U -n com.tinder -s tinder_scraper.js`  
4. **Extract Tokens:** Use Frida to retrieve `refresh_token`, `auth_token`, and `deviceId`.  

## Usage  
1. **Initialize the API:**  
   ```python  
   from main import TinderAccount  
   refresh_token = "YOUR_REFRESH_TOKEN"  
   auth_token = "YOUR_AUTH_TOKEN"  
   deviceId = "YOUR_DEVICE_ID"  
   proxies_list = []  # Optional proxies  
   test = TinderAccount(refresh_token, auth_token, deviceId, proxies=proxies_list)  
Fetch Profiles:
data = test.search()
Change Location:
test.changeLocation(lat=40.7128, long=-74.0060)
Update Filters:
test.ageDistanceChange(age_filter_max=30, age_filter_min=20, distance_filter=10)
Change Preferences:
test.interstedIn([0, 1])
Regenerate Auth Tokens:
test.authGen()
Check Authentication:
test.checkAuth()
Update Passport Location:
test.passport(lat=34.0522, long=-118.2437)
Notes
Run Frida once per account to retrieve the necessary tokens.
Proxies are optional but recommended for large-scale scraping.
Dependencies
requests
protobuf
protobuf-decoder
frida-tools
