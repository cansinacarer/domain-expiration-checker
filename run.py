from decouple import config
from app import check_domain_expiration_date
import time

if __name__ == "__main__":
    domain = config("DOMAIN")
    while True:
        check_domain_expiration_date(domain)
        time.sleep(60)
