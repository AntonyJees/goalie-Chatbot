from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# --- Mock League Match Data ---
MOCK_MATCHES = {
    "premier league": [
        {
            "team1": "Manchester United",
            "team2": "Chelsea",
            "time": "18:30",
            "venue": "Old Trafford"
        },
        {
            "team1": "Arsenal",
            "team2": "Liverpool",
            "time": "21:00",
            "venue": "Emirates Stadium"
        },
        {
            "team1": "Manchester City",
            "team2": "Tottenham",
            "time": "16:00",
            "venue": "Etihad Stadium"
        },
        {
            "team1": "Newcastle",
            "team2": "Aston Villa",
            "time": "14:00",
            "venue": "St James' Park"
        }
    ],

    "la liga": [
        {
            "team1": "Barcelona",
            "team2": "Sevilla",
            "time": "19:00",
            "venue": "Camp Nou"
        },
        {
            "team1": "Real Madrid",
            "team2": "Valencia",
            "time": "22:00",
            "venue": "Santiago Bernabéu"
        },
        {
            "team1": "Athletic Bilbao",
            "team2": "Real Betis",
            "time": "17:30",
            "venue": "San Mamés"
        },
        {
            "team1": "Atletico Madrid",
            "team2": "Villarreal",
            "time": "20:00",
            "venue": "Cívitas Metropolitano"
        }
    ],

    "bundesliga": [
        {
            "team1": "Bayern Munich",
            "team2": "Dortmund",
            "time": "17:00",
            "venue": "Allianz Arena"
        },
        {
            "team1": "RB Leipzig",
            "team2": "Bayer Leverkusen",
            "time": "15:30",
            "venue": "Red Bull Arena"
        },
        {
            "team1": "Wolfsburg",
            "team2": "Stuttgart",
            "time": "18:00",
            "venue": "Volkswagen Arena"
        }
    ],

    "serie a": [
        {
            "team1": "Juventus",
            "team2": "AC Milan",
            "time": "20:45",
            "venue": "Allianz Stadium"
        },
        {
            "team1": "Inter Milan",
            "team2": "Napoli",
            "time": "18:30",
            "venue": "San Siro"
        },
        {
            "team1": "Roma",
            "team2": "Lazio",
            "time": "16:00",
            "venue": "Stadio Olimpico"
        }
    ],

    "ligue 1": [
        {
            "team1": "PSG",
            "team2": "Lyon",
            "time": "21:00",
            "venue": "Parc des Princes"
        },
        {
            "team1": "Marseille",
            "team2": "Nice",
            "time": "18:00",
            "venue": "Stade Vélodrome"
        },
        {
            "team1": "Monaco",
            "team2": "Lille",
            "time": "15:00",
            "venue": "Stade Louis-II"
        }
    ],

    "mls": [
        {
            "team1": "LA Galaxy",
            "team2": "Seattle Sounders",
            "time": "19:30",
            "venue": "Dignity Health Sports Park"
        },
        {
            "team1": "Inter Miami",
            "team2": "Atlanta United",
            "time": "21:00",
            "venue": "Chase Stadium"
        }
    ],

    "indian super league": [
        {
            "team1": "Kerala Blasters",
            "team2": "Bengaluru FC",
            "time": "19:00",
            "venue": "Jawaharlal Nehru Stadium (Kochi)"
        },
        {
            "team1": "FC Goa",
            "team2": "Mumbai City FC",
            "time": "21:30",
            "venue": "Fatorda Stadium"
        },
        {
            "team1": "NorthEast United",
            "team2": "Hyderabad FC",
            "time": "17:00",
            "venue": "Indira Gandhi Athletic Stadium"
        }
    ],

    "champions league": [
        {
            "team1": "Real Madrid",
            "team2": "Bayern Munich",
            "time": "20:00",
            "venue": "Santiago Bernabéu"
        },
        {
            "team1": "Liverpool",
            "team2": "Barcelona",
            "time": "22:00",
            "venue": "Anfield"
        }
    ]
}


class ActionLeagueMatchesToday(Action):

    def name(self) -> Text:
        return "action_league_schedule"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        league = tracker.get_slot("league")

        if not league:
            dispatcher.utter_message(text="Which league do you mean?")
            return []

        league_lower = league.lower()

        # Fetch mock match list
        matches = MOCK_MATCHES.get(league_lower)

        if not matches:
            dispatcher.utter_message(
                text=f"Sorry, I couldn't find today's matches for {league}."
            )
            return []

       # Build response message
        response = f"📅 Today's matches in {league.title()}\n\n"

        for match in matches:
            response += (
            f"⚽ {match['team1']} vs {match['team2']}\n"
            f"⏱ Time: {match['time']}\n"
            f"📍 Venue: {match['venue']}\n"
            "-----------------------------\n"
            )

        dispatcher.utter_message(text=response)
        return []
