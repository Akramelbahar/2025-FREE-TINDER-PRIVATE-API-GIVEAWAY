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
# Guide to Extract Refresh Token and Device ID Using Frida

This guide explains how to extract the `refresh_token` and `deviceId` from the Tinder app using Frida and a rooted Android emulator.

---

## Prerequisites

1. **Rooted Android Emulator**  
   - Install **MEmu** from its official site.  
   - Enable **Root Mode**: Go to `Settings > Developer Options` and activate Root.  

2. **Frida Installation**  
   - Install Frida tools on your system using Python:  
     ```bash
     pip install frida-tools
     ```

3. **Tinder APK**  
   - Download the latest Tinder APK from a trusted source.  
   - Install it in the MEmu emulator by dragging and dropping the APK file.  

4. **Custom Frida Script**  
   - Prepare a Frida script (e.g., `tinder_scraper.js`) to hook into Tinder's authentication functions.

---

## Step-by-Step Guide

### Step 1: Launch MEmu and Tinder App
- Open the MEmu emulator.  
- Launch the Tinder app and log in with your account.

---

### Step 2: Attach Frida to Tinder
1. Connect Frida to the emulator:  
   ```bash
   frida -U -n com.tinder -s tinder_scraper.js
-U: Connect to the USB or emulator device.
-n com.tinder: Specifies the Tinder app.
-s tinder_scraper.js: Runs your custom Frida script.
