import json
import random

class DataHelper:

    def get_random_item(self, item_type):
        """
        Returns a random player or team depending on the item_type.
        item_type should be either 'player' or 'club'
        """

        file_map = {
            "player": "data/players.json",
            "club": "data/clubs.json",
            "competition": "data/competitions.json"
        }

        if item_type not in file_map:
            raise ValueError("item_type must be either 'player' or 'club' or 'competition'")

        file_path = file_map[item_type]

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # handle both file structures
        key = "players" if item_type == "player" else ("clubs" if item_type == "club" else "competitions")
        items = data[key] if key in data else data

        return random.choice(items)
