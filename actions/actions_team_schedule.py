from typing import Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.data_helper import DataHelper
from datetime import datetime, timedelta, time
import random

class ActionNextMatchSchedule(Action):

    def name(self) -> Text:
        return "action_next_match_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        team = next(tracker.get_latest_entity_values("team"), None)

        if not team:
            dispatcher.utter_message(text="Please tell me which team's next match you want to know.")
            return []

        venues = ["Camp Nou", "Santiago Bernabéu", "Allianz Arena", "Old Trafford", "San Siro"]

        mock_schedules = {
            "opponent": DataHelper.get_random_item(self, "club"),
            "date": datetime.now() + timedelta(days=10),
            "time": time(19, 30),
            "venue": random.choice(venues)
        }

        response = (
            f"🏟 Next Match Scheduled for {team}\n\n"
            f"🤝 Opponent: {mock_schedules['opponent']}\n"
            f"📅 Date: {mock_schedules['date'].strftime('%d %b %Y')}\n"
            f"⏰ Time: {mock_schedules['time'].strftime('%H:%M')}\n"
            f"📍 Venue: {mock_schedules['venue']}\n\n"
            f"🔥 Get ready for an exciting match!"
)

        dispatcher.utter_message(text=response)
        return []
