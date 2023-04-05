import re
import json
import random
from api import data
from faker import Faker
from api.role import Role


fake = Faker()

def parse_photo_url(url):
    pattern = ".*\/.*\/.\/(.*)\/.*"
    result = re.findall(pattern, url)
    id = result[0]

    return f"https://drive.google.com/uc?export=view&id={id}"



with open("./data/people.json", "r") as file, open("./mentors.sql", "w") as sql:
    people = json.load(file)
    id = 30
    
    for person in people:
        first_name = person['first_name']
        last_name = person['last_name']
        photo_url = parse_photo_url(person['photo_url'])

        bio = fake.text()
        field = random.choice(data.fields)
        level = random.choice(data.levels)

        skills_count = random.randint(1, len(data.skills))
        skills = ", ".join(random.sample(data.skills, skills_count))

        email = fake.email()

        user = f"""INSERT INTO public."user"
        (id, created_at, email, first_name, last_name, profile_photo, "role")
        VALUES({id}, 'now()', '{email}', '{first_name}', '{last_name}', '{photo_url}', '{Role.MENTEE.value}');\n"""
        
        mentee = f"""INSERT INTO public.mentee
        (bio, experience_field, experience_level, skills, mentee_id, calendar_id)
        VALUES('{bio}', '{field}', '{level}', '{skills}', {id}, '');\n"""

        mentor = f"""INSERT INTO public.mentor
        (mentor_id)
        VALUES({id});\n\n"""

        id += 1

        sql.write(user)
        sql.write(mentee)
        sql.write(mentor)


print("done!")

            