from auth import login_user
from data_processor import process_data


def main():
    print("Starting application...")  # ❌ No logging used
    user = login_user("admin", "supersecret")
    if user:
        data = process_data([1, 2, 3])
        print("Data processed:", data)  # ❌ Using print instead of logger


if __name__ == "__main__":
    main()
