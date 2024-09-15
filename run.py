from decouple import config
from app import check_domain_updated_date
import time

if __name__ == "__main__":
    domain = config("DOMAIN")
    UPDATE_PERIOD = config("UPDATE_PERIOD", cast=int)
    while True:
        check_domain_updated_date(domain)
        time.sleep(UPDATE_PERIOD)
