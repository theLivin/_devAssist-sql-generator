import random
import textwrap
from api import data
from faker import Faker
from api.role import Role


fake = Faker()

class User:
    COLUMNS = ["id", "email", "first_name", "last_name", "role", "profile_photo", "created_at"]
    PHOTO_URL = "https://xsgames.co/randomusers/assets/avatars/"

    def __init__(self, id=random.randint(1, 10), role=Role.DEFAULT.value):
        self.id = str(id)
        self.role = role

        self.created_at = "now()"

        profile = fake.profile()
        name = profile['name'].split()
        self.first_name = name[0]
        self.last_name = name[-1]
        self.email = profile['mail']
        
        self.profile_photo = User.PHOTO_URL
        sex = profile['sex']
        if sex == 'M':
            self.profile_photo += "male"
        elif sex == 'F':
            self.profile_photo += "female"
        
        self.profile_photo += "/"+str(id%79)+".jpg"

        self.bio = fake.text()
        self.field = random.choice(data.fields)
        self.level = random.choice(data.levels)

        skills_count = random.randint(1, len(data.skills))
        self.skills = ", ".join(random.sample(data.skills, skills_count))

    def __repr__(self) -> str:
        return f"""{','.join(val if val.isdigit() else f"'{val}'" for val in self.data())}"""

    def data(self):
        return [str(self.id), self.email, self.first_name, self.last_name, self.role, self.profile_photo, self.created_at]
    
    def insert(self):
        return textwrap.dedent(f'''insert into "user" ({','.join(f'"{col}"' for col in User.COLUMNS)}) values ({self});\n''')


class OnboardedUser:
    COLUMNS = ["user_id", "bio", "experience_field", "experience_level", "skills"]

    def __init__(self, id=random.randint(1, 10)):
        self.id = str(id)
        self.bio = fake.text()
        self.field = random.choice(data.fields)
        self.level = random.choice(data.levels)

        skills_count = random.randint(1, len(data.skills))
        self.skills = ", ".join(random.sample(data.skills, skills_count))
    
    def __repr__(self) -> str:
        return f"""{','.join(val if val.isdigit() else f"'{val}'" for val in self.data())}"""

    def data(self):
        return [self.id, self.bio, self.field, self.level, self.skills]
