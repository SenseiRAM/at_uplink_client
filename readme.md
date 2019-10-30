### Airtable Uplink API Client
This is a not terribly beautiful app to backup a given Airtable table
to a CSV. It uses Uplink to create an API client, which returns 
JSON, which is then parsed into a CSV by Pandas.

I'm putting this up mainly for posterity. I'm working on a 
better solution that uses Python Airtable Wrapper and Python's 
own CSV module.

Note that you'll need to input your own AT base key and API 
key. Also, since data is being returned in string format, 
you have to specify user locale and timezone in the query 
string. Info for setting locale is [here](https://support.airtable.com/hc/en-us/articles/220340268-Supported-locale-modifiers-for-SET-LOCALE).
Info for setting timezone is [here](https://support.airtable.com/hc/en-us/articles/216141558-Supported-timezones-for-SET-TIMEZONE).