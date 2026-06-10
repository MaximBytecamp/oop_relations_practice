class Player:
    def __init__(self, nickname: str, age: int, rating: int):
        self.nickname = nickname
        self.age = age
        self.rating = rating

    def get_profile(self) -> str:
        return f"{self.nickname}, рейтинг: {self.rating}"

    def get_impact(self) -> float:
        raise NotImplementedError("Метод нужно переопределить")


class FPSPlayer(Player):
    def __init__(self, nickname: str, age: int, rating: int, accuracy: float):
        super().__init__(nickname, age, rating)
        self.accuracy = accuracy

    def get_impact(self) -> float:
        # TODO: придумать формулу полезности FPS-игрока
        pass


class MOBAPlayer(Player):
    def __init__(self, nickname: str, age: int, rating: int, average_kda: float):
        super().__init__(nickname, age, rating)
        self.average_kda = average_kda

    def get_impact(self) -> float:
        # TODO: придумать формулу полезности MOBA-игрока
        pass


class Team:
    def __init__(self, title: str):
        self.title = title
        self.players = []

    def add_player(self, player: Player):
        # TODO: добавить уже существующего игрока
        pass


player_1 = FPSPlayer("ByteSniper", 18, 2400, accuracy=71.5)
player_2 = MOBAPlayer("MidStorm", 19, 2200, average_kda=4.8)

team = Team("TOP Arena")
team.add_player(player_1)
team.add_player(player_2)

team.print_roster()
print("Общая полезность:", team.get_total_impact())
