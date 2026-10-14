import dotenv as de
import os


def load_configs() -> dict[str, str | None]:

    de.load_dotenv()

    required_keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    config = {}
    for key in required_keys:
        config[key] = os.getenv(key)

    return config


def validate_config(config: dict[
        str, str | None
        ]) -> bool:

    valid = True
    for key, value in config.items():
        if not value:
            print(f"[MISSING] '{key}'")
            valid = False
        else:
            print(f"[OK] '{key}'")
    return valid


def display_environment(
        config: dict[str, str | None]
        ) -> None:
    mode = config["MATRIX_MODE"]
    if mode == "development":

        print("Working in development mode.\n")
        for key, value in config.items():
            status = "Configured" if value else "Missing"
            if key == "API_KEY":
                print(f"API Access: {status}")
            elif key == "DATABASE_URL":
                print(f"Database: {status}")
            elif key == "ZION_ENDPOINT":
                print(f"Zion Network: {status}")
            elif key == "MATRIX_MODE":
                print(f"Mode: {value}")
            elif key == "LOG_LEVEL":
                print(f"Log level: {value}")

    elif mode == "production":
        print("Working in production mode")
        print("Sensitive configuration values are hidden")

    else:
        print(
            "MATRIX_MODE is missing or invalid."
            )


def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_configs()

    valid = validate_config(config)
    if valid:
        print("Configuration loaded.\n")
    else:
        print("Warning incomplete configuration.")
    print()
    display_environment(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
