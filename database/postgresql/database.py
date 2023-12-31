from database.utils import get_postgres_credentials
import psycopg2

def select_images():
    images = []
    try:
        user, password = get_postgres_credentials()
        conn = psycopg2.connect(
            user = user,
            password = password,
            host = "localhost",
            port = "5432",
            database = "portfolio"
        )
        cur = conn.cursor() 
        cur.execute("select name, url, description, url_full_size, tags from images")
        images = cur.fetchall()
        print(images)
    
        #fermeture de la connexion à la base de données
        cur.close()
        conn.close()
    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)
    return images



