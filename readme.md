# Domain Expiration Checker
This is my small Dockerized app that checks whether the expiration date of a domain has changed every minute. When a change in expiration date is found, it sends an email to the address specified in the environment variables.

## Deployment
You can use the `Dockerfile` to deploy this app. You will need to specify the domain, notification email, and SMTP credentials as environment variables, using the names described in `.env.template`.

## Running locally
1. Create a virtual environment:
   ```sh
   python -m venv env
   ```
2. Activate the virtual environment:
    ```sh
    source env/bin/activate
    ```
3. Create the environment variables shown in the `.env.template` file.
   
4. Run the script
    ```sh
    python main.py
    ```
