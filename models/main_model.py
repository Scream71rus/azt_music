
class MainModel():
    async def get_password(self, login):
        sql = "select * from azt.customer where login = %s"
        cursor = await self.db.execute(sql, (login,))

        return cursor.fetchone()

    async def set_db_cookie(self, cookie, customer_id):
        sql = "insert into azt.cookie(customer_id, cookie) values(%s, %s)"
        await self.db.execute(sql, (customer_id, cookie))

    async def get_customer(self, cookie):
        sql = "select * from azt.customer where id = (select customer_id from azt.cookie where cookie = %s)"
        cursor = await self.db.execute(sql, (cookie,))

        return cursor.fetchone()

    async def check_login(self, login):
        sql = "select id from azt.customer where login = %s"
        cursor = await self.db.execute(sql, (login,))

        return cursor.fetchone()

    async def create_customer(self, login, password, salt):
        sql = "insert into azt.customer(login, password, salt) values(%s, %s, %s) RETURNING id"
        cursor = await self.db.execute(sql, (login, password, salt))

        return cursor.fetchone()
