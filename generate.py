from faker import Faker
import random
import data

fake = Faker()


print("-- mentors --")
start_id = int(input('start at: '))
num = int(input('count: '))

user_cols = ["id", "email", "first_name", "last_name", "role", "profile_photo"]
def users():
    for i in range(start_id, start_id + num):
        profile = fake.profile()
        name = profile['name'].split()
        firstname = name[0]
        lastname = name[-1]
        sex = profile['sex']
        profile_photo = "https://xsgames.co/randomusers/assets/avatars/"
        if sex == 'M':
            profile_photo += "male"
        elif sex == 'F':
            profile_photo += "female"
        profile_photo += "/"+str(i%79)+".jpg"
        
        yield [str(i), profile['mail'], firstname, lastname, '0', profile_photo]


mentor_cols = ["mentor_id", "bio", "experience_field", "experience_level", "skills"]
def mentors():
    for user in users():
        field = random.choice(data.fields)
        level = random.choice(data.levels)

        skills_count = random.randint(1, len(data.skills))
        skills = ", ".join(random.sample(data.skills, skills_count))

        yield [user[0], fake.text(), field, level, skills]


user_query = f'''
insert into "user" ({','.join(f'"{col}"' for col in user_cols)}) values 
{','.join([f"""({','.join(u if u.isdigit() else f"'{u}'" for u in user)})""" for user in users()])};
'''

mentor_query = f'''
insert into "mentor" ({','.join(f'"{col}"' for col in mentor_cols)}) values 
{','.join([f"""({','.join(m if m.isdigit() else f"'{m}'" for m in mentor)})""" for mentor in mentors()])};
'''

with open('populate.sql', 'w') as sql_file:
    sql_file.write("-- populate user table")
    sql_file.write(user_query)
    sql_file.write("\n")
    sql_file.write("-- populate mentor table")
    sql_file.write(mentor_query)
