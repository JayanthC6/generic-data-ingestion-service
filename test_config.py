from app.config.config_loader import ConfigLoader

print(ConfigLoader.load("jsonplaceholder"))

print()

print(ConfigLoader.available_sources())