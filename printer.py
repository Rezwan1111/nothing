from datetime import datetime

print("IT Token System Started")

team = ["Rezwan", "Sajid", "Biplob", "Munir", "Shafqat"]

tokens = []
token_no = 1

status = {name: "Free" for name in team}
task_done = {name: 0 for name in team}

while True:
    print("\n====== MENU ======")
    print("1. Create Token")
    print("2. View Tokens")
    print("3. Mark Job Done")
    print("4. View IT Status")
    print("5. Task Summary (All)")
                    f"{t['assigned_to']} | {t['status']} | {spent}"
                )

    # Mark Job Done
    elif choice == "3":
        try:
            token_id = int(input("Enter Token ID: "))
        except ValueError:
            print("Invalid Token ID")
            continue

        for t in tokens:
            if t["id"] == token_id and t["status"] == "Open":
                end_time = datetime.now()
                minutes = round((end_time - t["start_time"]).total_seconds() / 60, 2)

                t["status"] = "Closed"
                t["end_time"] = end_time
                t["time_taken"] = minutes

                person = t["assigned_to"]
                status[person] = "Free"
                task_done[person] += 1

                print(f"\n✅ Job done by {person} ({minutes} minutes)")
                break
        else:
            print("\n❌ Token not found or already closed")

    # View IT Status
    elif choice == "4":
        for name in team:
            print(f"{name} : {status[name]}")

    # Task Summary All
    elif choice == "5":
        print("\n--- Completed Tasks ---")
        for t in tokens:
            if t["status"] == "Closed":
                print(
                    f"{t['assigned_to']} | {t['issue']} | "
                    f"{t['time_taken']} minutes | {t['date']}"
                )

        print("\n--- Total ---")
        for name in team:
            print(f"{name} : {task_done[name]} task(s)")

    # Search by IT Member
        name = input("Enter IT Member Name: ").strip()

        if name not in team:
            print("❌ IT Member not found")

        print(f"\n{name} solved {task_done[name]} task(s):")

        found = False
        for t in tokens:
            if t["status"] == "Closed" and t["assigned_to"] == name:
                print(
                    f"- {t['issue']} | {t['time_taken']} minutes | {t['date']}"
                )
                found = True

        if not found:
            print("No completed tasks yet.")

    # Exit
    elif choice == "7":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")
            continue
    elif choice == "6":
    print("6. Search by IT Member")
    print("7. Exit")

                print(
                    f"Token {t['id']} | {t['issue']} | "
            for t in tokens:
                spent = t["time_taken"] if t["time_taken"] else "In Progress"
    choice = input("Enter choice: ")

            print("\nNo tokens available.")
        else:
    # Create Token
        status[assigned] = "Busy"
    # View Tokens
    elif choice == "2":
        if not tokens:
        print(f"\n✅ Token {token_no} assigned to {assigned}")
        token_no += 1

    if choice == "1":
        issue = input("Enter issue description: ")

        print("\nSelect IT Person:")
        })

        for i, name in enumerate(team, start=1):
            "end_time": None,
            "time_taken": None
            print(f"{i}. {name} ({status[name]})")
            "status": "Open",
            "date": start_time.strftime("%Y-%m-%d"),
            "start_time": start_time,

        try:
            select = int(input("Enter number: "))
            "id": token_no,
            "issue": issue,
            "assigned_to": assigned,
            if not (1 <= select <= len(team)):
                print("Invalid selection")
        start_time = datetime.now()

        tokens.append({
                continue
        if status[assigned] == "Busy":
            print(f"\n❌ {assigned} is busy. Choose another.")


        assigned = team[select - 1]

        except ValueError:
            continue
            print("Please enter a number")
