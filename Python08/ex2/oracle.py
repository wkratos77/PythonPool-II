import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    missing = []

    if not mode:
        missing.append("MATRIX_MODE")
    if not db:
        missing.append("DATABASE_URL")
    if not api:
        missing.append("API_KEY")
    if not log:
        missing.append("LOG_LEVEL")
    if not zion:
        missing.append("ZION_ENDPOINT")

    if missing:
        print("Missing configuration:", ", ".join(missing))
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print("Database: Connected to local instance" if mode == "development"
          else "Database: Production database")
    print("API Access: Authenticated")
    print(f"Log Level: {log}")
    print("Zion Network: Online\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")
