from . import conn_cur, commit_and_close


class Series:
    keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

    def __init__(self, serie, seasons, released_date, genre, imdb_rating) -> None:
        self.serie = serie.title()
        self.seasons = seasons
        self.released_date = released_date
        self.genre = genre.title()
        self.imdb_rating = imdb_rating


    @staticmethod
    def create_table_if_not_exists():
        
        conn, cur = conn_cur()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS ka_series(
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) UNIQUE NOT NULL,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            );
        """
        )

        commit_and_close(conn, cur)

        return 'created'


    def create_serie(self):
        Series.create_table_if_not_exists()

        conn, cur = conn_cur()

        query = """
            INSERT INTO
                ka_series
            (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = list(self.__dict__.values())

        cur.execute(query, query_values)

        inserted_data = cur.fetchone()

        commit_and_close(conn, cur)

        return dict(zip(self.keys, inserted_data))

    @staticmethod
    def get_all():

        conn, cur = conn_cur()

        cur.execute(
            """
            SELECT * FROM ka_series;
        """
        )

        users = cur.fetchall()

        commit_and_close(conn, cur)

        users_found = [dict(zip(Series.keys, user)) for user in users]

        return users_found


    @staticmethod
    def get_by_id(id):

        conn, cur = conn_cur()

        cur.execute(
            """
            SELECT * FROM ka_series WHERE id=(%s);
        """,
            (id,),
        )

        user = cur.fetchone()

        user_found = dict(zip(Series.keys, user))

        commit_and_close(conn, cur)

        return user_found

    