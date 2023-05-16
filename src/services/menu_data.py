from src.models.dish import Dish, Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.create_recipe()

    def read_csv(self):
        with open(self.path) as file:
            data_reader = csv.DictReader(file)
            users_list_dic = []
            for list_users in data_reader:
                users_list_dic.append(list_users)
        return users_list_dic

    def create_recipe(self):
        data = self.read_csv()
        recipe_exits = {}
        for item in data:
            if item["dish"] in recipe_exits:
                recipe_exits[item["dish"]].add_ingredient_dependency(
                    Ingredient(item["ingredient"]), int(item["recipe_amount"]))
            else:
                recipe_exits[item["dish"]] = Dish(
                    item["dish"], float(item["price"])
                )
                recipe_exits[item["dish"]].add_ingredient_dependency(
                    Ingredient(item["ingredient"]), int(item["recipe_amount"]))
        for dish in recipe_exits.values():
            self.dishes.add(dish)
