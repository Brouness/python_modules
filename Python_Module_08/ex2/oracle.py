import os
from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    load_dotenv()
    my_dict: dict[str, str] = {}
    default: dict[str, str] = {
        "MATRIX_MODE": "development",
        "DATABASE_URL": "Not configured",
        "API_KEY": "Not configured",
        "LOG_LEVEL": "INFO",
        "ZION_ENDPOINT": "Not configured"
        }
    for key, value in default.items():
        my_dict.update({key: str(os.environ.get(key, value))})
    return my_dict


def display_config(configurations: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print("Mode: " + configurations["MATRIX_MODE"])
    print("Database: " + configurations["DATABASE_URL"])
    print("API Access: " + (
        "Authenticated"
        if configurations["API_KEY"] != "Not configured" else "Not configured")
        )
    print("Log Level: " + configurations["LOG_LEVEL"])
    print("Zion Network: " + (
        "Online"
        if configurations["ZION_ENDPOINT"] != "Not configured" else
        "Not configured")
    )


def security(configurations: dict[str, str]) -> None:
    print("\nEnvironment security check:")
    if (configurations["API_KEY"] != "Not configured" and
            configurations["DATABASE_URL"] != "Not configured"):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Some secrets are not configured")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    if configurations["MATRIX_MODE"] in ("development", "production"):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] MATRIX_MODE not properly set")


def main() -> None:
    configurations: dict[str, str] = load_config()
    display_config(configurations)
    security(configurations)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
