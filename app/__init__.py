import whois
import os
from app.email import send_notification_for_domain_expiration

EXPIRATION_DATE_FILE = os.path.join(os.path.dirname(__file__), "expiration_date.txt")


def check_domain_expiration_date(domain):
    # Get the last known expiration date of the domain from file
    if os.path.exists(EXPIRATION_DATE_FILE):
        with open(EXPIRATION_DATE_FILE, "r") as file:
            last_known_date = file.read()
    else:
        # Create the file if it doesn't exist
        with open(EXPIRATION_DATE_FILE, "w") as file:
            last_known_date = "unknown"

    # Get the expiration date of the domain
    try:
        results = whois.whois(domain)
        print(f"The expiration date of {domain} is {results.expiration_date}")

        # Compare the expiration date with the last known date
        if str(results.expiration_date) != last_known_date:
            # Save the new expiration date to the file
            with open(EXPIRATION_DATE_FILE, "w") as file:
                file.write(str(results.expiration_date))

            # Print info about the change
            print(
                f"Expiration date for {domain} has changed from {last_known_date} to {results.expiration_date}"
            )

            # Send an email notification
            send_notification_for_domain_expiration(domain, results)

    except Exception as e:
        print(f"An error occurred during whois lookup:\n{e}")
