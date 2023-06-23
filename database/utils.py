import os

def get_postgres_credentials():
    return (
        os.getenv("POSTGRES_USER"),
        os.getenv("POSTGRES_PASSWORD"),
    )