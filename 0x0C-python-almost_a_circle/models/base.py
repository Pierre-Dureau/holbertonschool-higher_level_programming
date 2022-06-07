#!/usr/bin/python3
"""Module Base"""
import json
import os
import csv
import turtle
import random


class Base():
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Get the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string(None))
            else:
                s = []
                for obj in list_objs:
                    s.append(obj.to_dictionary())
                f.write(cls.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """Get the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Get an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Get a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                list_str = cls.from_json_string(f.read())
                list_ins = []
                for str in list_str:
                    list_ins.append(cls.create(**str))
                return list_ins
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is None:
                f.write()
                return
            fieldnamesR = ["id", "width", "height", "x", "y"]
            fieldnamesS = ["id", "size", "x", "y"]
            if cls.__name__ == "Rectangle":
                writer = csv.DictWriter(f, fieldnames=fieldnamesR)
            else:
                writer = csv.DictWriter(f, fieldnames=fieldnamesS)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                filecontent = csv.DictReader(f)
                list_obj = []
                for row in filecontent:
                    for key, value in row.items():
                        row[key] = int(value)
                    list_obj.append(cls.create(**row))
                return list_obj
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares"""
        color = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'pink']

        turtle.shape("turtle")
        turtle.color("green")
        turtle.pensize(5)
        turtle.speed(2)

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x * 2, rect.y * 2)
            turtle.pendown()
            turtle.pencolor(color[random.randint(0, 6)])
            for i in range(2):
                turtle.forward(rect.width * 2)
                turtle.left(90)
                turtle.forward(rect.height * 2)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x * 2, square.y * 2)
            turtle.pendown()
            turtle.pencolor(color[random.randint(0, 6)])
            for i in range(2):
                turtle.forward(square.width * 2)
                turtle.left(90)
                turtle.forward(square.height * 2)
                turtle.left(90)

        turtle.exitonclick()
