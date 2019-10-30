from at_client import ATSearchClient
import requests.exceptions
import pandas
from datetime import datetime
import winsound  # Optional if you want program to beep when finished

# TODO add exceptions for bad requests (no internet connection, etc)


def main():
    print('Welcome to AT Backup!')
    get_all_records()
    beep() # Optional if you want program to beep when finished


def get_all_records():
    # Keep any existing spaces in the table string.
    # It will automagically be formatted in the API request
    table_string = "NAME OF YOUR TABLE"
    at_client = ATSearchClient()
    response = at_client.get_first_records_page(table_string)
    response.raise_for_status()
    results = response.json()
    data = [item for item in results['records']]

    if 'offset' in results:
        data = get_remaining_records(results, data, at_client, table_string)

    today = datetime.strftime(datetime.now(), "%b-%d-%Y %H%M")
    frame = pandas.DataFrame.from_records(data)
    frame.to_csv(f'2020 Applications Backup {today}.csv')


def get_remaining_records(json_results, first_page_data, client, table_name):
    offset = json_results['offset']
    while True:
        response = client.get_next_records_page(table_name, offset)
        response.raise_for_status()
        results = response.json()
        for item in results['records']:
            first_page_data.append(item)
        if 'offset' in results:
            offset = results['offset']
        else:
            return first_page_data


def beep():
    frequency = 2000  # Set Frequency To 2500 Hertz
    duration = 250  # Set Duration To 1000 ms == 1 second

    for _ in range(3):
        winsound.Beep(frequency, duration)


if __name__ == '__main__':
    main()
