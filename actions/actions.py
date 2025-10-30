from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import yaml
from pathlib import Path


def load_api_config():
    config_path = Path(__file__).parent.parent / "endpoints.yml"
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config.get("api", {}) 

class ActionShowLeagueMatches(Action):

    def name(self) -> str:
        return "action_show_league_matches"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        league = tracker.get_slot("league")
        country = tracker.get_slot("country")
        print(f"League: {league}, Country: {country}")

        if not league or not country:
            dispatcher.utter_message(text="Please tell me both the league and country.")
            return []

        api_url = "https://v3.football.api-sports.io/leagues"
        headers = {"x-apisports-key": "YOUR_API_KEY"}
        params = {"country": country, "name": league}

        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()

        if "response" in data and data["response"]:
            league_info = data["response"][0]["league"]
            message = f"✅ {league_info['name']} from {country} is available for season {league_info['season']}."
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=f"Sorry, I couldn't find {league} from {country}.")

        return []



































# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import json
# from pathlib import Path
# from difflib import get_close_matches

# class ActionGetLeagues(Action):
#     def name(self) -> str:
#         return "action_get_leagues"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict):
        
#         country = tracker.get_slot("country")
#         if not country:
#             dispatcher.utter_message(text="Please tell me which country you're interested in.")
#             return []
        


# class ActionGetCountryCode(Action):

#     def name(self) -> str:
#         return "action_get_country_code"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict):

#         # Get the country name from the entity
#         user_country = tracker.get_slot("country_name")

#         if not user_country:
#             dispatcher.utter_message(text="Please tell me a country name.")
#             return []

#         # Path to your countries.json file
#         file_path = Path(__file__).parent.parent / "data" / "countries.json"

#         # Load countries
#         with open(file_path, "r", encoding="utf-8") as f:
#             countries = json.load(f)["countries"]

#         # Fuzzy match for handling typos
#         country_names = [c["name"] for c in countries]
#         match = get_close_matches(user_country, country_names, n=1, cutoff=0.6)

#         if match:
#             country = next(c for c in countries if c["name"] == match[0])
#             dispatcher.utter_message(
#                 text=f"The country code for {country['name']} is {country['code']}."
#             )
#         else:
#             dispatcher.utter_message(
#                 text=f"Sorry, I couldn't find a country matching '{user_country}'."
#             )

#         return []
    
# import requests

# class ApiClient:
#     """
#     A reusable class for making external API calls.
#     Supports GET, POST, PUT, DELETE requests with optional headers and parameters.
#     """

#     def __init__(self, base_url, default_headers=None, timeout=10):
#         """
#         Initialize the API client.
#         :param base_url: Base URL for the API
#         :param default_headers: Default headers for all requests (optional)
#         :param timeout: Timeout for requests in seconds (default: 10)
#         """
#         self.base_url = base_url.rstrip('/')
#         self.default_headers = default_headers or {}
#         self.timeout = timeout

#     def _make_request(self, method, endpoint, **kwargs):
#         """
#         Internal method to make an API request.
#         :param method: HTTP method (GET, POST, PUT, DELETE)
#         :param endpoint: API endpoint (path after base URL)
#         :param kwargs: Additional arguments (headers, params, json, data, etc.)
#         :return: JSON response or None
#         """
#         url = f"{self.base_url}/{endpoint.lstrip('/')}"
#         headers = {**self.default_headers, **(kwargs.pop("headers") or {})}


#         try:
#             response = requests.request(
#                 method=method,
#                 url=url,
#                 headers=headers,
#                 timeout=self.timeout,
#                 **kwargs
#             )
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.Timeout:
#             print(f"Request to {url} timed out.")
#         except requests.exceptions.RequestException as e:
#             print(f"Error during {method.upper()} request to {url}: {e}")
#         return None

#     def get(self, endpoint, params=None, headers=None):
#         return self._make_request("GET", endpoint, params=params, headers=headers)

#     def post(self, endpoint, data=None, json=None, headers=None):
#         return self._make_request("POST", endpoint, data=data, json=json, headers=headers)

#     def put(self, endpoint, data=None, json=None, headers=None):
#         return self._make_request("PUT", endpoint, data=data, json=json, headers=headers)

#     def delete(self, endpoint, headers=None):
#         return self._make_request("DELETE", endpoint, headers=headers)
    
# API_KEY = "758c280f1a7f6a92f504b65658fdceef"

# api = ApiClient(
#     base_url="https://v3.football.api-sports.io",
#     default_headers={"x-rapidapi-key": API_KEY}
# )

# response = api.get("/leagues", params={"country": "england"})
# print(response)


