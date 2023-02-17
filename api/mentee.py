import textwrap
from api.user import User, OnboardedUser
import random

class Mentee(OnboardedUser):
    COLUMNS = ["mentee_id", "bio", "experience_field", "experience_level", "skills"]

    def __init__(self, id=random.randint(1, 10)):
        super().__init__(id)
        self.user = User(id)

    def insert(self):
        q =  textwrap.dedent(f'''insert into "mentee" ({','.join(f'"{col}"' for col in Mentee.COLUMNS)}) values ({self});''')
        return textwrap.dedent(f'''{self.user.insert()}{q}\n''')