#!/usr/bin/python3
""" Module that contains class Base """
import json
import csv
import os.path
import turtle


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        dico = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                dico.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(dico)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ is 'Square':
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []
        try:
            with open(filename, 'r') as f:
                list_str = f.read()

            list_cls = cls.from_json_string(list_str)
            list_ins = []

            for index in range(len(list_cls)):
                list_ins.append(cls.create(**list_cls[index]))
            return list_ins

        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        try:
            with open(filename, 'r') as readFile:
                reader = csv.reader(readFile)
                csv_list = list(reader)

            if cls.__name__ == "Rectangle":
                list_keys = ['id', 'width', 'height', 'x', 'y']
            else:
                list_keys = ['id', 'size', 'x', 'y']

            matrix = []

            for csv_elem in csv_list:
                dict_csv = {}
                for kv in enumerate(csv_elem):
                    dict_csv[list_keys[kv[0]]] = int(kv[1])
                matrix.append(dict_csv)

            list_ins = []

            for index in range(len(matrix)):
                list_ins.append(cls.create(**matrix[index]))
        except IOError:
            return []

        return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module """
        turt = turtle.Turtle()
        turt.pensize(3)

        turt.color("#0000ff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
