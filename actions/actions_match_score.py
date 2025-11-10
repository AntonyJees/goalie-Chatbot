from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import json

class ActionShowMatchScore(Action):
    def name(self) -> str:
        return "action_show_match_score"
    
    def getRandomPlayer(self):
    
        file_path = "data/players.json"
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        players = data["players"]

        return random.choice(players)

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        

        teams = [e['value'] for e in tracker.latest_message.get('entities', []) if e['entity'] == 'team']

        
        print("teams extracted:", teams)
        
        if len(teams) < 2:
            dispatcher.utter_message(text="⚠️ I need two team names to show the match result.")
            return []

        team1, team2 = teams[0].capitalize(), teams[1].capitalize()

        print("ActionShowPlayerStats triggered")
        if not team1 or not team2:
            dispatcher.utter_message(text="Please provide both team names to get the match score.")
            return []


        team1_score = random.randint(0, 5)
        team2_score = random.randint(0, 5)

        team1_goal_scores = []
        team2_goal_scores = []
        for _ in range(team1_score):
            team1_goal_scores.append(self.getRandomPlayer())
        for _ in range(team2_score):
            team2_goal_scores.append(self.getRandomPlayer())

        # Sample match data
        match = {
            "team1": team1,
            "team2": team2,
            "team1_score": team1_score,
            "team2_score": team2_score,
            "status": "Full Time",
            "team1_scorers": team1_goal_scores,
            "team2_scorers": team2_goal_scores,
            "date": "2025-11-05",
            "competition": "Premier League"
        }

        match_result = f"""🏟 Match Result: {match['team1']} vs {match['team2']}
        Score: {match['team1']} {match['team1_score']} - {match['team2_score']} {match['team2']}
        Status: {match['status']}
        Goal Scorers:
            {match['team1']}: {' | '.join(match['team1_scorers']) if match['team1_scorers'] else 'None'}
            {match['team2']}: {' | '.join(match['team2_scorers']) if match['team2_scorers'] else 'None'}
        Date: {match['date']}
        Competition: {match['competition']}
        """


        print(match_result)

        dispatcher.utter_message(text=match_result)