import yaml
from pathlib import Path

class ApiConfig:
    
    @staticmethod
    def get_api_config():
        config_path = Path(__file__).parent.parent / "endpoints.yml"
        try:
            with open(config_path, "r") as file:
                config = yaml.safe_load(file)
            api = config.get("api", {})
            return {
                "base_url": api.get("football_base_url"),
                "api_key": api.get("football_api_key")
            }
        except Exception as e:
            print(f"Error loading endpoints.yml: {e}")
            return {}
