import textwrap
from api.role import Role
from api.user import User
from api.mentee import Mentee
import random

class Mentor:
    COLUMNS = ["mentor_id"]

    def __init__(self, id=random.randint(1, 10)):
        self.id = str(id)
        self.mentee = Mentee(id)

    def __repr__(self) -> str:
        return f"""{','.join(val if val.isdigit() else f"'{val}'" for val in self.data())}"""

    def data(self):
        return [self.id]

    def insert(self):
        q =  textwrap.dedent(f'''insert into "mentor" ({','.join(f'"{col}"' for col in Mentor.COLUMNS)}) values ({self});''')
        return textwrap.dedent(f'''{self.mentee.insert()}{q}\n''')