from pathlib import Path
import yaml


CONFIG_DIR = Path(__file__).resolve().parents[2] / "configs"


class ConfigLoader:

    @staticmethod
    def load(source_name: str):

        config_file = CONFIG_DIR / f"{source_name}.yaml"

        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration '{source_name}.yaml' not found."
            )

        with open(config_file, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    @staticmethod
    def available_sources():

        return sorted(
            file.stem
            for file in CONFIG_DIR.glob("*.yaml")
        )