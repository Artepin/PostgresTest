import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Postgres:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password='1111',
                                               host="127.0.0.1",
                                               port='5432')
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor = self.connection.cursor()
        except(Exception, Error) as error:
            print('Ошибка при работе с PostgresSQL ', error)

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с базой данных закрыто")

    def create_db(self):
        # создание базы данных
        sql_create_db = 'create database postgres_db'
        self.cursor.execute(sql_create_db)

    def get_db_info(self):
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(self.connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        self.cursor.execute("SELECT version();")
        # Получить результат
        record = self.cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    def create_db(self):
        # создание базы данных
        sql_create_db = 'create database postgres_db'
        self.cursor.execute(sql_create_db)

    def get_db_info(self):
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(self.connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        self.cursor.execute("SELECT version();")
        # Получить результат
        record = self.cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    def create_table(self):
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE mobile
                                     (ID INT PRIMARY KEY     NOT NULL,
                                     MODEL           TEXT    NOT NULL,
                                     PRICE         REAL); '''
        # Выполнение команды: это создает новую таблицу
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    def get_table(self, table_name):
        # Выполнение SQL-запроса для возврата содержимого таблицы по её имени
        get_table_request = 'SELECT * FROM ' + table_name
        self.cursor.execute(get_table_request)
        record = self.cursor.fetchall()
        print(record)

    def add_data(self):
        # Выполнение SQL-запроса для вставки данных в таблицу
        insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (2, 'SamsungS20+', 500)"""
        self.cursor.execute(insert_query)
        self.connection.commit()
        print("1 запись успешно вставлена")

    def update_data(self):
        # Выполнение SQL-запроса для обновления таблицы
        update_query = """Update mobile set price = 1111 where id = 1"""
        self.cursor.execute(update_query)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Запись успешно изменена")

    def remove_data(self):
        # Выполнение SQL-запроса для удаления таблицы
        delete_query = """Delete from mobile where id = 1"""
        self.cursor.execute(delete_query)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Запись успешно удалена")


def main():
    db = Postgres()
    db.update_data()
    db.get_table('mobile')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
