## Update Preferences Script for Bluesky API
This Python script updates user preferences on the Bluesky platform using their API. The script utilizes a Bearer token for authorization.
It is just a way to have your birthdate set to 0001-01-01 

## IT WILL CHANGES YOUR TAGS you'll have to update them after

Prerequisites
Python 3.x installed on your system.
requests library installed. Run the following command to install it:
```bash
pip install requests
```
## Usage
1. Setting Up the Script
Clone or download this repository.
Open the script.py file and locate the following section:
```python
TOKEN = ""
```
Replace the empty string "" with your Bearer token (instructions below).

## 2. Obtaining Your Bearer Token
To interact with Bluesky's API, you need an authorization Bearer token. Follow these steps to retrieve it using your web browser:

Step 1: Open Bluesky in Your Browser
  - Navigate to Bluesky and log in to your account.
Step 2: Open Developer Tools
  - Press F12 or Ctrl+Shift+I (on Windows/Linux) or Cmd+Option+I (on macOS) to open the Developer Tools.
  Go to the Network tab.
Step 3: Filter Requests
  - In the search bar, filter network requests by typing putPreferences or looking for a similar API request.
Step 4: Capture the Request
- Perform an action in the Bluesky app that triggers an API call, such as saving preferences.
  Look for a request to a URL similar to:
      https://poisonpie.us-west.host.bsky.network/xrpc/app.bsky.actor.putPreferences
  Click on the request in the Network tab.
Step 5: Find the Bearer Token
  - Under the Headers section of the request details:
  Scroll to the Authorization header.
  Copy the token value after Bearer.

## 3. Running the Script
Paste the token into the TOKEN variable in the script.
Run the script:
```bash
python main.py
```
If successful, the script will update the preferences and output:
```
Birthdate updated successfully!
```
Otherwise, it will display an error message with details.

##Notes
Token Privacy: Never share your Bearer token as it grants access to your account.
Error Handling: Ensure that the API endpoint and payload structure align with Bluesky’s documentation. A 401 status typically indicates an invalid or expired token.

## Disclaimer
This script is for educational purposes only. Use it responsibly and comply with Bluesky’s terms of service.
