import psycopg2

with psycopg2.connect(host='localhost', user= 'postgres', password='Alireza13', dbname='Pagila', port=5432) as conn:
    with conn.cursor() as cur:
        cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
        for table in cur.fetchall():
            print(table) 