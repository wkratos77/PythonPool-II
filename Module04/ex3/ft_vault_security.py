if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating vault security protocols...")
    file_content = ""

    try:
        with open("classified_data.txt", "r") as file:
            file_content = file.read()
            print("Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION:")
        print(file_content)
        print()
        print("SECURE PRESERVATION:")

        with open("classified_data.txt", "w") as file:
            file.write("[CLASSIFIED] New security protocols archived\n")

        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
        print()
        print("All vault operations completed with maximum security.")

    except Exception:
        print("Connection failed")
