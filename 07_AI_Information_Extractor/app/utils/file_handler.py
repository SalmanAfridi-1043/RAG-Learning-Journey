import json
from pathlib import Path

FILE_PATH = Path("app/storage/extracted_data.json")


def save_data(data: dict):

    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    if FILE_PATH.exists():
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            records = json.load(file)
    else:
        records = []

    records.append(data)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

    print("\nInformation saved successfully!")


def get_saved_data():

    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
