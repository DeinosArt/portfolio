import psycopg2

def select_images():
    # import postgresql
    # db = postgresql.get_db()
    # return db.select("images")
    try:
        conn = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = "5432",
            database = "portfolio"
        )
        cur = conn.cursor()
        # Afficher la version de PostgreSQL 
        cur.execute("select * from images")
        images = cur.fetchall()
        print("Images : ", images,"\n")
    
        #fermeture de la connexion à la base de données
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)
    return []

select_images()
