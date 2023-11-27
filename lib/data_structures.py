spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("spiciness", 0) > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "unknown")
        cuisine = food.get("cuisine", "unknown")
        spiciness = food.get("spiciness", 0)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]


def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat // len(spicy_foods)
    return average


def create_spicy_food(spicy_foods, spicy_food):
    pass
