from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import json
from actions.data_helper import DataHelper
import datetime

class ActionShowMatchScore(Action):
    def name(self) -> str:
        return "action_show_match_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        teams = [
                    e['value'].strip().title()
                    for e in tracker.latest_message.get('entities', [])
                    if e.get('entity') == 'team'
                ]

        print("Teams extracted:", teams)
        if len(teams) == 0:
            dispatcher.utter_message(
                text="⚠️ I need at least one team name to show the match result. Please specify a team."
            )
            return []
        
        if len(teams) < 2:
            team1 = teams[0]
            team2 = DataHelper.get_random_item(self, "club")
        else:   
            team1, team2 = teams[0], teams[1]

        print(f"Team 1: {team1}, Team 2: {team2}")

        team1_score = random.randint(0, 5)
        team2_score = random.randint(0, 5)

        team1_goal_scores = []
        team2_goal_scores = []
        for _ in range(team1_score):
            team1_goal_scores.append(DataHelper.get_random_item(self, "player") + f" ({random.randint(1,90)}')")
        for _ in range(team2_score):
            team2_goal_scores.append(DataHelper.get_random_item(self, "player") + f" ({random.randint(1,90)}')")

        # Sample match data
        match = {
            "team1": team1,
            "team2": team2,
            "team1_score": team1_score,
            "team2_score": team2_score,
            "status": "Full Time",
            "team1_scorers": team1_goal_scores,
            "team2_scorers": team2_goal_scores,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "competition": DataHelper.get_random_item(self, "competition")
        }

        match_result = f"""⚽️ Match Result ⚽️

            🏟 {match['team1']} vs {match['team2']}
            📝 Score: {match['team1_score']} - {match['team2_score']}
            ⏱ Status: {match['status']}
            📅 Date: {match['date']}
            🏆 Competition: {match['competition']}

            🔥 Goal Scorers:
               - {match['team1']}: {' | '.join(match['team1_scorers']) if match['team1_scorers'] else 'None'}
               - {match['team2']}: {' | '.join(match['team2_scorers']) if match['team2_scorers'] else 'None'}
    """



        print(match_result)

        dispatcher.utter_message(text=match_result)