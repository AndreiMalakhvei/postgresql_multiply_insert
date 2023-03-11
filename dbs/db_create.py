import psycopg2
from dbs.secret_keys_db import POSTGRE_SECRET_KEYS
from psycopg2 import extras as ext


class PostgresqlDB:
    DBNAME = POSTGRE_SECRET_KEYS['DBNAME']
    USER = POSTGRE_SECRET_KEYS['USER']
    PASSWORD = POSTGRE_SECRET_KEYS['PASSWORD']
    HOST = POSTGRE_SECRET_KEYS['HOST']

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostgresqlDB, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def table_create():
        with psycopg2.connect(dbname=PostgresqlDB.DBNAME, user=PostgresqlDB.USER, password=PostgresqlDB.PASSWORD,
                              host=PostgresqlDB.HOST) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS testing(
                        id serial PRIMARY KEY,
                    link CHARACTER VARYING(300),
                    reference CHARACTER VARYING(30),
                    price INTEGER,
                    title CHARACTER VARYING(1000),                        
                    pubdate TIMESTAMP WITH TIME ZONE,
                    areas NUMERIC(7, 2),
                    city CHARACTER VARYING(30),
                    address CHARACTER VARYING(1000),
                    region CHARACTER VARYING(30),
                    rooms INTEGER,
                    exyear INTEGER,
                    seller CHARACTER VARYING(1000),
                    is_tg_posted BOOLEAN DEFAULT FALSE,
                    is_archived BOOLEAN DEFAULT FALSE,
                    photo_qty INTEGER,
                    photo_links  TEXT,
                    description TEXT

                        )''')

    @staticmethod
    def save_single_record(obj):
        with psycopg2.connect(dbname=PostgresqlDB.DBNAME, user=PostgresqlDB.USER, password=PostgresqlDB.PASSWORD,
                              host=PostgresqlDB.HOST) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                        INSERT INTO testing (link, reference, price, title, description, pubdate,areas,city,address,region,rooms,
                        exyear,seller, photo_links, photo_qty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)                                      
                         ''',
                            (obj.link, obj.reference, obj.price, obj.title, obj.description, obj.pubdate,
                             obj.areas, obj.city, obj.address, obj.region, obj.rooms, obj.exyear,
                             obj.seller, ','.join(obj.photo_links), obj.photo_qty)
                            )

    @staticmethod
    def save_batch(data_tuple):
        with psycopg2.connect(dbname=PostgresqlDB.DBNAME, user=PostgresqlDB.USER, password=PostgresqlDB.PASSWORD,
                              host=PostgresqlDB.HOST) as conn:
            with conn.cursor() as cur:
                ext.execute_batch(cur, '''
                        INSERT INTO testing (link, reference, price, title, description, pubdate,areas,city,address,
                        region,rooms,exyear,seller, photo_links, photo_qty)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)                                        
                         ''',
                            data_tuple, page_size=1000
                            )

    @staticmethod
    def save_tuple_one_by_one(data_tuple):
        with psycopg2.connect(dbname=PostgresqlDB.DBNAME, user=PostgresqlDB.USER, password=PostgresqlDB.PASSWORD,
                              host=PostgresqlDB.HOST) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                        INSERT INTO testing (link, reference, price, title, description, pubdate,areas,city,address,
                        region,rooms,exyear,seller, photo_links, photo_qty)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)                                      
                         ''',
                            (data_tuple)

                            )

    @staticmethod
    def save_values(obj_list):
        with psycopg2.connect(dbname=PostgresqlDB.DBNAME, user=PostgresqlDB.USER, password=PostgresqlDB.PASSWORD,
                              host=PostgresqlDB.HOST) as conn:
            with conn.cursor() as cur:
                ext.execute_values(cur, ''' INSERT INTO testing (link, reference, price, title, description, pubdate,areas,city,address,
                        region,rooms,exyear,seller, photo_links, photo_qty) VALUES %s''',
                                   [(
                             obj.link, obj.reference, obj.price, obj.title, obj.description, obj.pubdate,
                             obj.areas, obj.city, obj.address, obj.region, obj.rooms, obj.exyear,
                             obj.seller, ','.join(obj.photo_links), obj.photo_qty) for obj in obj_list], page_size=1000)

    @staticmethod
    def delete_all():
        with psycopg2.connect(dbname=PostgresqlDB.DBNAME, user=PostgresqlDB.USER, password=PostgresqlDB.PASSWORD,
                              host=PostgresqlDB.HOST) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    DELETE FROM testing
                        ''')