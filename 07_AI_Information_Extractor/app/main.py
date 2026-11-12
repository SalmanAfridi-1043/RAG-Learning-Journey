from app.services.extractor import extract_information
from app.utils.file_handler import save_data
from app.utils.file_handler import save_data, get_saved_data


def view_records():

    records = get_saved_data()

    if not records:
        print("\nNo saved records found!")
        return

    print("\n---------- SAVED RECORDS ----------")

    for index, record in enumerate(records, start=1):
        print(f"\n\nRecord: {index}")
        print("-" * 40)

        for key, value in record.items():
            print(f"{key.capitalize()}: {value}")


def main():

    print()
    print("-" * 45)
    print("       AI INFORMATION EXTRACTOR")
    print("-" * 45)

    while True:
        text = input("\nEnter text ('view' to see records, 'exit' to quit): ")

        if text.lower().strip() == "exit":
            print("\n---------- Chat Ended ----------\n")
            break

        if not text.strip():
            print("Please enter some text!")
            continue

        if text.lower().strip() == "view":
            view_records()
            continue

        try:
            result = extract_information(text)

            print("\n--- EXTRACTED INFORMATION ---")
            print(result.model_dump_json(indent=4))

            # save the model response in storage
            save_data(result.model_dump())

        except (ValueError, RuntimeError) as e:
            print(f"\nError: {e}")


# used to prevent main() to be executed automatically when other files import it.
if __name__ == "__main__":
    main()


# Exactly! It prevents main() from executing automatically when another file imports main.py.
