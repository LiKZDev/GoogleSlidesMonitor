import sys
import requests
from requests.exceptions import InvalidSchema

# URL to call
url = "https://docs.google.com/presentation/d/e/2PACX-1vQTtYXI2JV-3qIcQg2SMcEr0jpM0LnxpPX--W1-qAimaSIPoie-LNiri6cjMfhFvhrJH-i294exp6gv/embed?start=false&loop=false&delayms=60000"

# Last known hash and revision number CAA 21 March 2019
expected_hmac = "ALf4PZ4AY0kYH6IzG9YRAz-9R-sUTzd4hg"
expected_revision = "211.0"

isChanged = False

if len(sys.argv) > 1:
  url = sys.argv[1]

  if len(sys.argv) > 2:
    expected_hmac = sys.argv[2]
    expected_revision = ""

    if len(sys.argv) > 3:
      expected_revision = sys.argv[3]

try:
  print("----------------------------------------------------------------------------------------")
  print("Calling url " + url)
  print("----------------------------------------------------------------------------------------")

  # Calls the request URL
  r = requests.get(url)

  # Extract response text
  content = r.text

  # Extract hmac from response text
  content = content[content.find("viewerHmac: '") + 13:]
  response_hmac = content[:content.find("'")]

  # Extract revision number from response text
  content = content[content.find("revision:  ") + 11:]
  response_revision = content[:content.find(" ,")]

  print("Expected HMAC: " + expected_hmac)
  print("Actual HMAC  : " + response_hmac + "\n")

  if response_hmac != expected_hmac:
    isChanged = True

  if expected_revision:
    print("Expected Revision: " + expected_revision)
    print("Actual Revision  : " + response_revision + "\n")

    if response_revision != expected_revision:
      isChanged = True

  if isChanged:
    print('\x1b[0;30;41m' + 'The slide has been changed' + '\x1b[0m')
  else:
    print('\x1b[6;30;42m' + 'The slide is the same' + '\x1b[0m')

except InvalidSchema as invalid_schema_error:
  print("The url provided is unavailable")
  print(invalid_schema_error)
