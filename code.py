import os
import sys
from twocaptcha import TwoCaptcha

api_key = "f8345b4b5aedff92b7c1171a7a499fdb"

solver = TwoCaptcha(api_key)

# Use absolute path to the image
captcha_path = r'D:\HSP\test1.png'

# Check if the file exists
if not os.path.exists(captcha_path):
    print(f"Error: CAPTCHA file not found at {captcha_path}")
    sys.exit(1)

try:
    result = solver.normal(captcha_path)
except Exception as e:
    print(f"Error solving CAPTCHA: {e}")
    sys.exit(1)
else:
    print('Solved CAPTCHA:', result)
    sys.exit(0)

