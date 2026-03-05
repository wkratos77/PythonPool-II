import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    id_vr = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()
    sys.stdout.write(f"[STANDARD] Archive status from {id_vr}: {status}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
        )
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")
