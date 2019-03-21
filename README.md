# GoogleSlidesMonitor
Python Script to monitor any changes made to Google Slides

## Getting Started
Download and copy slides_checker.py into your home directory
```
cp slides_checker.py ~
```

### Running slides_checker.py
To run slides_checker.py, use the following command 
```
python slides_checker.py <url> <expected_hmac> <expected_revision_number>
```
- `url` (Optional)
URL of the google slides you wish to check
- `expected_hmac` (Optional)
The current HMAC for the google slides
- `expected_revision_number` (Optional)
The current revision number for the google slides

**Note: If no arguments is applied, the default values for the slides are:**
- `url = "https://docs.google.com/presentation/d/e/2PACX-1vQTtYXI2JV-3qIcQg2SMcEr0jpM0LnxpPX--W1-qAimaSIPoie-LNiri6cjMfhFvhrJH-i294exp6gv/embed?start=false&loop=false&delayms=60000"`
- `expected_hmac = "ALf4PZ4AY0kYH6IzG9YRAz-9R-sUTzd4hg"`
- `expected_revision_number = "221.0"`

### Running slides_checker.py using cron
Add a cronjob to run the checker every minute 
1. Open cron
```
crontab -e
```
2. Add the following line at the end of your crontab.

**Note: To insert using the vim editor, press `i`. To save, type `!wq`**
```
*/1 * * * * /usr/bin/python ~/slides_checker.py
```
