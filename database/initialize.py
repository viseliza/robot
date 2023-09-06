import sqlite3
import logging

def create_db():
    with sqlite3.connect("sqlite3.db") as con:
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER,
                group_id INTEGER
            )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        ''')

        """
            TODO:
            Добавить запросы на INSERT групп, если таковых нет, чтобы пробрасывать все группы ещё перед стартом работы бота
        """

class User:
    async def add(id: int):
        pass

    async def get(id: int):
        pass
    
    async def update(id: int):
        pass

    async def delete(id: int):
        pass

    async def exists(id: int):
        # Пытаемся найти пользователя
        exists = await User.get(id)

        # Debug лог
        logging.debug(f'UserExists: User={id}, Exists={bool(exists)}')

        # Если не существует - добавляем
        if not bool(exists):
            await User.add(id)

        # Возврат ответа
        return exists


class Group:
    async def add(id: int):
        pass

    async def get(name: str):
        pass
    
    async def update(id: int):
        pass

    async def delete(id: int):
        pass
