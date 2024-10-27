import random

class FunRandomName:
    def __init__(self):
        self.__adjectives = ["Сумасшедший", "Грустный", "Волосатый", "Лысый", "Глупый"]
        self.__nouns = ["Мальчик", "Бабушка", "Охранник", "Девочка", "Жук"]

    def get_name(self, *args, **kwargs) -> str:
        return f"{random.choice(self.__adjectives)} {random.choice(self.__nouns)}"
    
    def add_adjective(self, adjective: str):
        self.__adjectives.append(adjective)

    def add_noun(self, noun: str):
        self.__nouns.append(noun)

    def get_all_names(self) -> list:
        return [f"{adj} {noun}" for adj in self.__adjectives for noun in self.__nouns]

    def get_total_adjectives(self) -> int:
        return len(self.__adjectives)

    def get_total_nouns(self) -> int:
        return len(self.__nouns)

if __name__ == "__main__":
    name_generator = FunRandomName()
    print("Забавное имя:", name_generator.get_name())
