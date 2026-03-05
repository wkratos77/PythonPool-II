def crisis_handler(filename: str, routine: bool) -> None:
    if routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"SUCCESS: Archive recovered - ''{content}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    crisis_handler("lost_archive.txt", routine=False)
    print()
    crisis_handler("classified_vault.txt", routine=False)
    print()
    crisis_handler("standard_archive.txt", routine=True)

    print()
    print("All crisis scenarios handled successfully. Archives secure.")
