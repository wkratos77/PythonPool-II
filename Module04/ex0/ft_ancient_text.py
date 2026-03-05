if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        exit()
    print("Connection established...")
    file_txt = file.read()
    print()
    print("RECOVERED DATA:")
    print(file_txt)
    file.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")
