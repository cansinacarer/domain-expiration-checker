import whois
from decouple import config
import os
from app.email import (
    send_notification_for_whois_update,
    send_notification_for_error,
)

UPDATE_DATE_FILE = os.path.join(os.path.dirname(__file__), "updated_date.txt")
ERROR_COUNT_BEFORE_EMAIL = config("ERROR_COUNT_BEFORE_EMAIL", cast=int)


def check_domain_updated_date(domain):
    # Get the last known updated date of the domain from file
    if os.path.exists(UPDATE_DATE_FILE):
        with open(UPDATE_DATE_FILE, "r") as file:
            last_known_date = file.read()
    else:
        # Create the file if it doesn't exist
        with open(UPDATE_DATE_FILE, "w") as file:
            last_known_date = "unknown"

    # Get the updated date of the domain
    try:
        # Whois Lookup
        results = whois.whois(domain)

        # If we reached here without an error, report the date and reset error counter
        print(f"The updated date of {domain} is {results.updated_date}")
        error_count = 0

        # Compare the updated date with the last known date
        if str(results.updated_date) != last_known_date:
            # Save the new updated date to the file
            with open(UPDATE_DATE_FILE, "w") as file:
                file.write(str(results.updated_date))

            # Print info about the change
            print(
                f"Whois update date for {domain} has changed from {last_known_date} to {results.updated_date}"
            )

            # Send an email notification
            send_notification_for_whois_update(domain, results)

    except Exception as e:
        print(f"An error occurred during whois lookup:\n{e}")
        error_count += 1

        # If we exceeded the number of consecutive errors allowed before email notification, notify
        if error_count > ERROR_COUNT_BEFORE_EMAIL:
            send_notification_for_error(domain)
