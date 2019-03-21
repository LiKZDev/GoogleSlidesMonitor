import requests
import json

hmac = "ALf4PZ4AY0kYH6IzG9YRAz-9R-sUTzd4hg"
revision = "211.0"

success = True

webhook_url = 'xxxx' # Slack webhook URL

try:
  r = requests.get(
  "https://docs.google.com/presentation/d/e/2PACX-1vQTtYXI2JV-3qIcQg2SMcEr0jpM0LnxpPX--W1-qAimaSIPoie-LNiri6cjMfhFvhrJH-i294exp6gv/embed?start=false&loop=false&delayms=60000")

  content = r.text

  content = content[content.find("viewerHmac: '") + 13:]
  response_hmac = content[:content.find("'")]

  content = content[content.find("revision:  ") + 11:]
  response_revision = content[:content.find(" ,")]

  print(response_hmac)
  print(response_revision)

  if response_hmac == hmac:
    print("HMAC is the same")
  else:
    print("Slide is edited")
    success = False

  if response_revision == revision:
    print("Revision is the same")
  else:
    print("Slide is edited")
    success = False


  if not success:
    payload = {
      "channel": "#alarms",
      "username": "Script Alert",
      "text": "Slide is edited",
      "icon_emoji": ":warning:"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if response.status_code != 200:
      raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
      )
except:
  payload = {
    "channel": "#alarms",
    "username": "Script Alert",
    "text": "Content provider is unavailable",
    "icon_emoji": ":warning:"
  }
  response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

  if response.status_code != 200:
    raise ValueError(
      'Request to slack returned an error %s, the response is:\n%s'
      % (response.status_code, response.text)
    )

