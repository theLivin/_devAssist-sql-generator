import textwrap
from api.user import User, OnboardedUser
import random

class Mentor(OnboardedUser):
    COLUMNS = ["mentor_id", "bio", "experience_field", "experience_level", "skills"]

    def __init__(self, id=random.randint(1, 10)):
        super().__init__(id)
        self.user = User(id)

    def insert(self):
        q =  textwrap.dedent(f'''insert into "mentor" ({','.join(f'"{col}"' for col in Mentor.COLUMNS)}) values ({self});''')
        return textwrap.dedent(f'''{self.user.insert()}{q}\n''')