import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        """Создает таблицу questions, если она не существует."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            question TEXT NOT NULL
        );
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def add_question(self, question):
        """Добавляет вопрос в базу данных."""
        insert_query = sql.SQL("INSERT INTO questions (question) VALUES (%s);")
        self.cursor.execute(insert_query, (question,))
        self.conn.commit()

    def get_random_question(self):
        """Возвращает случайный вопрос из базы данных."""
        select_query = "SELECT question FROM questions ORDER BY RANDOM() LIMIT 1;"
        self.cursor.execute(select_query)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_all_questions(self):
        """Возвращает все вопросы из базы данных."""
        select_query = "SELECT question FROM questions;"
        self.cursor.execute(select_query)
        return [row[0] for row in self.cursor.fetchall()]

    def delete_question(self, question_id):
        """Удаляет вопрос по его ID."""
        delete_query = sql.SQL("DELETE FROM questions WHERE id = %s;")
        self.cursor.execute(delete_query, (question_id,))
        self.conn.commit()

    def close(self):
        """Закрывает соединение с базой данных."""
        self.cursor.close()
        self.conn.close()