import jwt
from datetime import datetime
from datetime import timedelta
import calendar
​
# Variables
private_key = b"-----BEGIN RSA PRIVATE KEY-----\nMIIE..."
five_minutes_expiry = datetime.now() + timedelta(minutes=5)   # If setting expiry date/time in future
unixtime = calendar.timegm(five_minutes_expiry.utctimetuple())

# Encode and create token
encoded = jwt.encode({PAYLOAD}, private_key, algorithm="RS384")
print(encoded)
