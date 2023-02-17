import textwrap
from api.user import User, OnboardedUser
import random

class Mentor(OnboardedUser):
    COLUMNS = OnboardedUser.COLUMNS
    COLUMNS[0] = "mentor_id"

    def __init__(self, id=random.randint(1, 10)):
        super().__init__(id)
        self.user = User(id)

    def insert(self):
        q =  textwrap.dedent(f'''insert into "mentor" ({','.join(f'"{col}"' for col in self.COLUMNS)}) values ({self});''')
        return textwrap.dedent(f'''{self.user.insert()}{q}\n''')