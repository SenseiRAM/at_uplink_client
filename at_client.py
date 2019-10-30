import requests
import uplink
import os

AIRTABLE_API_KEY = os.environ['AIRTABLE_API_KEY']

@uplink.headers({
    "Authorization": f"Bearer {AIRTABLE_API_KEY}"
})
@uplink.json
class ATSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url=f"https://api.airtable.com/v0/YOUR BASE KEY")


    @uplink.get("{table_name}?"
                "cellFormat=string"
                "&timeZone='America/Chicago'"  # Adjust if necessary
                "&userLocale='en-nz'"  # Preferred date format
                "&view=NAME OF VIEW")  # Put the name of the view here, I use one with all fields visible
    def get_first_records_page(self, table_name):
        """ Gets first page of Airtable records """ \

    @uplink.get("{table_name}?"
                "cellFormat=string"
                "&timeZone='America/Chicago'"  # Adjust if necessary
                "&userLocale='en-nz'"  # Preferred date format
                "&offset={offset}"
                "&view=NAME OF FIELDS")  # Must be the same as the view name used in get_first_records_page
    def get_next_records_page(self, table_name, offset):
        """ If there are multiple pages, gets remaining Airtable records """
