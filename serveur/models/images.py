import database.db_mock as db_mock
import database.postgresql as postgresql



def get_images(use_mock):
    images = []
    if use_mock:
        images = db_mock.select_images()
    else:
        images = postgresql.select_images()
    return images
