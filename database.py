import sqlite3

conn = sqlite3.connect('animals.db')

c = conn.cursor()


# c.execute("""Create TABLE animals (
#             name TEXT,
#             cass TEXT,
#             desc TEXT,
#             dang TEXT,
#             pic BLOB,
#             cons TEXT
# )""")


class Animal:

    def __init__(self, name, cass, description, danger, pic, conservation_status):
        # Name is name
        self.name = name
        # cass refers to an animals class, such as reptile
        self.cass = cass
        # Animal physical description
        self.description = description
        # danger refers to what dangers the animal may pose.
        # EX: poisonous, seek medical attention if bitten
        self.danger = danger
        # This will be the animals pic, when this file was created
        # I was not whether to embed the pic or its file path
        self.pic = pic
        # cons is the animals conservation status
        self.conservation_status = conservation_status

    # This
    def __repr__(self):
        return "Ani('{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.cass, self.description,
                                                                self.danger, self.pic, self.conservation_status)


# function to add pics
def convert_pic(filename):
    with open(filename, 'rb') as file:
        photo = file.read()
    return photo


def insert_animal(animal):
    with conn:
        c.execute("""INSERT INTO animals VALUES (
                    :name, :cass, :description, :danger, :pic, :conservation_status
                    )""",
                  {'name': animal.name, 'cass': animal.cass,
                   'desc': animal.description, 'danger': animal.danger,
                   'pic': animal.pic, 'cons': animal.conservation_status})


def get_animal_by_name(name):
    c.execute("SELECT * FROM animals WHERE name=:name",
              {'name': name})
    return c.fetchall()


def remove_animal(name):
    with conn:
        c.execute("DELETE from animals WHERE name = :name",
                  {'name': name})


def get_all():
    c.execute("SELECT * FROM animals")
    return c.fetchall()


def get_animal_info(name):
    c.execute("SELECT name, cass, desc, dang, cons from animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


"""animal_1 = Animal(    # Format: name, cass, desc, dang, image, cons
                'Gopher Tortoise',
                'Reptile',
                'Georgia’s state reptile, the gopher tortoise is a large reptile adapted to burrowing. Gopher tortoises have a yellow bottom shell, with the rest of the tortoise being brown, or grey. Carapace length ranges from 6 to 9.5 in. Some examples are as large as 16 in. Gopher tortoises are herbivores, and their diet includes mushrooms, fruits, and grasses. They are known to live in colonies of several tortoises. The conservation status of these tortoises is important because they are a keystone species. The tortoises and their burrows are threatened by  habitat destruction and predation. Gopher tortoises are a keystone species because the burrows they make provide shelter for many other species.',
                'Not Dangerous',
                convert_pic("Gopherus_polyphemus_Tomfriedel.jpg"),
                'Vulnerable',
            )"""

"""
animal_ = Animal(    # Format: name, cass, desc, dang, image, cons
                '',
                '',
                '',
                '',
                convert_pic(""),
                '',
                )
"""

# insert_animal(animal_1)

print(get_animal_info('Copperhead'))

# c.execute("SELECT * FROM animals")
# print(c.fetchone())

# animals = get_animal_by_name('American Alligator')
# animals = get_all()
# print(animals)

conn.close()
