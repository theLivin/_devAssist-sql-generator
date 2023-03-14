import textwrap
import random
from faker import Faker
import random
from api.mentee import Mentee

from api.mentor import Mentor

fake = Faker()

def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

class Review:
    COLUMNS = ["id", "created_at", "updated_at", "review", "mentee_id", "mentor_id", "rating"]

    def __init__(self, id=random.randint(1, 10), mentor_id=random.randint(1, 10), mentee_id=random.randint(1, 10)):
        self.id = str(id)
        self.created_at = "now()"
        self.updated_at = "now()"
        self.review = fake.text()
        self.mentor_id = str(mentor_id)
        self.mentee_id = str(mentee_id)
        self.mentor = Mentor(mentor_id)
        self.mentee = Mentee(mentee_id)
        self.rating = "{:.2f}".format((random.random()*10)+1)


    def __repr__(self) -> str:
        return f"""{','.join(val if val.isdigit() or isfloat(val) else f"'{val}'" for val in self.data())}"""

    def data(self):
        return [str(self.id), self.created_at, self.updated_at, self.review, self.mentee_id, self.mentor_id, self.rating]
    
    def insert(self):
        q = textwrap.dedent(f'''insert into "review" ({','.join(f'"{col}"' for col in Review.COLUMNS)}) values ({self});''')
        return textwrap.dedent(f'''{self.mentor.insert()}{self.mentee.insert()}{q}\n''')