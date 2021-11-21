'''
accounts
'''
from dataclasses import dataclass


@dataclass
class Account:
    account_id: int
    account_name: str


class AccountsTable:
    def __init__(self, db_conn) -> None:
        self.db_conn = db_conn
        self.known_accounts = {}

    def get_id(self, account_name, insert_missing=True):
        try:
            account_id = self.known_accounts[account_name]
        except KeyError:
            if insert_missing is False:
                account_id = None
            else:
                account_id = self.select_id(account_name)
                if account_id is None:
                    account_id = self.insert_name(account_name)
                self.known_accounts[account_name] = account_id
        return account_id

    def select_id(self, account_name):
        sql = """
            select account_id
            from tro.accounts
            where account_name = %s
        """
        with self.db_conn.cursor() as cursor:
            cursor.execute(sql, (account_name,))
            results = cursor.fetchone()
        if results is None:
            account_id = None
        else:
            account_id = results[0]
        return account_id

    def insert_name(self, account_name):
        sql = "insert into tro.accounts (account_name) values (%s)"
        with self.db_conn.cursor() as cursor:
            cursor.execute(sql, (account_name,))

        account_id = self.select_id(account_name)
        return account_id

    def select_all_accounts(self):
        sql = """
            select account_name, account_id
            from tro.accounts
            order by account_name
        """
        with self.db_conn.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
        accounts = dict(results)
        return accounts


# def add_new_account(connection, account_name):
#     global known_accounts
#     log.debug(f'begin add_new_account({account_name})')

#     sql = "insert into tro.accounts (account_name) values (%s)"
#     with connection.cursor() as cursor:
#         cursor.execute(sql, (account_name,))

#     account_id = select_account_id(connection, account_name)

#     known_accounts[account_name] = account_id

#     log.debug(f'end   add_new_account - returns {account_id}')
#     return account_id
