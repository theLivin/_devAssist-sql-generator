import textwrap
from faker import Faker
import random
from api.mentee import Mentee
from api.mentor import Mentor

fake = Faker()

class Request:
    COLUMNS = ["id", "mentor_id", "mentee_id", "created_at", "updated_at", "message"]

    def __init__(self, id=random.randint(1, 10), mentor_id=random.randint(1, 10), mentee_id=random.randint(1, 10)):
        self.id = str(id)

        self.mentor_id = str(mentor_id)
        self.mentee_id = str(mentee_id)
        self.mentor = Mentor(mentor_id)
        self.mentee = Mentee(mentee_id)

        self.created_at = "now()"
        self.updated_at = "now()"
        self.message = fake.text()

    def __repr__(self) -> str:
        return f"""{','.join(val if val.isdigit() else f"'{val}'" for val in self.data())}"""

    def data(self):
        return [self.id, self.mentor_id, self.mentee_id, self.created_at, self.updated_at, self.message]
    
    def insert(self):
        q = textwrap.dedent(f'''insert into "request" ({','.join(f'"{col}"' for col in Request.COLUMNS)}) values ({self});''')

        return textwrap.dedent(f'''{self.mentor.insert()}{self.mentee.insert()}{q}\n''')