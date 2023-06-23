import database
import database.db_mock as db_mock
import database.postgresql as postgresql


def has_database():
    user, password = database.get_postgres_credentials()
    #return False
    return (
        user and password
    )


def get_images():
    images = []
    if has_database():
        images = postgresql.select_images()
    else:
        images = db_mock.select_images()
    return images
