# Here are my imports and such
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sqlite3

# Connecting to my database ---------------------------

conn = sqlite3.connect('animals.db')

c = conn.cursor()


# The class that works with the database
class Animals:

    def __init__(self, name, cass, description, danger, picture, conservation_status):
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
        self.picture = picture
        # cons is the animals conservation status
        self.conservation_status = conservation_status

    # This, repr is a formal function. it will be valid in many cases
    def __repr__(self):
        return "Animal('{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.cass, self.description,
                                                                   self.danger, self.picture,
                                                                   self.conservation_status)

    # starting functions that work with the database
    # The function to get the animal by name
    def get_animal_by_name(self):
        c.execute("SELECT * FROM animals WHERE name=:name",
                  {'name': self})
        return c.fetchall()

    # Function to get all the animals
    @staticmethod
    def get_all():
        c.execute("SELECT * FROM animals")
        return c.fetchall()

    # Function that gets the animals info by name without the picture. Used as a test
    def get_animal_info(name):
        c.execute("SELECT name, cass, desc, dang, cons FROM animals WHERE name = :name",
                  {'name': name})
        return c.fetchall()


def get_name_by_name(name):
    c.execute("SELECT name FROM animals WHERE name=:name",
              {'name': name})
    return c.fetchall()


def get_cass_by_name(name):
    c.execute("SELECT cass FROM animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


def get_description_by_name(name):
    c.execute("SELECT desc FROM animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


def get_danger_by_name(name):
    c.execute("SELECT dang FROM animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


def get_conservation_status_by_name(name):
    c.execute("SELECT cons FROM animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


def get_picture_by_name(name):
    c.execute("SELECT pic FROM animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


# The function to get the animal by name
def get_animal_by_name(name):
    c.execute("SELECT * FROM animals WHERE name=:name",
              {'name': name})
    return c.fetchall()


# Function to get all the animals
def get_all():
    c.execute("SELECT * FROM animals")
    return c.fetchall()


# Function that gets the animals info by name without the picture. Used as a test
def get_animal_info(name):
    c.execute("SELECT name, cass, desc, dang, cons FROM animals WHERE name = :name",
              {'name': name})
    return c.fetchall()


# Starting my Kivy classes ---------------------------------
# My Main Page Class
class MainPage(Screen):
    search = ObjectProperty()

    def search_btn(self):
        if Animals.get_animal_info(self.search.text):
            AnimalPage.current = self.search.text
            self.reset()
            sm.current = "animal"
        else:
            invalid_search()
            self.reset()
            sm.current = "main"

    def reset(self):
        self.search.text = ""


# This class will display the animals information


class AnimalPage(Screen):
    current = ""
    # Animal Name, has two ee so that it does not conflict with the screen name
    namee = ObjectProperty("Animal Name")
    # Animal Class
    cass = ObjectProperty("Animal Class")
    # Animal Conservation Status
    conservation_status = ObjectProperty("Conservation Status")
    #  Animal Description
    description = ObjectProperty("Animal Description")
    # Animal Danger
    danger = ObjectProperty("Animal Danger")
    # Animal Pic
    picture = ObjectProperty("Animal Picture")

    def on_enter(self, *args):
        print(get_animal_info(self.current))
        # n, cass, desc, dang, pic, cons = get_ani_by_name(self.current)
        self.namee = get_name_by_name(self.current)
        self.cass.str = get_cass_by_name(self.current)
        self.description.str = get_description_by_name(self.current)
        self.danger.str = get_danger_by_name(self.current)
        self.picture.image = get_picture_by_name(self.current)
        self.conservation_status.str = get_conservation_status_by_name(self.current)

    def back_to_main(self):
        sm.current = "main"


# This class is the screen manager
class WindowManager(ScreenManager):
    pass

    search = ObjectProperty("")


def invalid_search():
    pop = Popup(title='Invalid Search',
                content=Label(text='That is not an animal in the compendium\n'
                                   'check your spelling or search for another\n'
                                   'animal please'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


# Loading my kv file

kv = Builder.load_file("animalcompendium.kv")
# building another window manager
sm = WindowManager()

# listing my screens. This should enable me to switch via the python document in addition to my kv file.

screens = [MainPage(name="main"), AnimalPage(name="animal")]
for screen in screens:
    sm.add_widget(screen)

# This will reset the window

sm.current = "main"


# The App class

class AnimalCompendiumApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    AnimalCompendiumApp().run()
