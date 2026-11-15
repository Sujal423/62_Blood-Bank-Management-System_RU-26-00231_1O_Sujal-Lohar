# Blood Bank Management System
# Concepts used: Dictionaries, Lists, File Handling, Search

FILE_NAME = "donors.txt"

# Dictionary: blood group -> units available (initial stock)
stock = {
    "A+": 10, "A-": 0,
    "B+": 5,  "B-": 0,
    "O+": 8,  "O-": 0,
    "AB+": 2, "AB-": 0
}

# List of dictionaries: each donor is {"name": ..., "group": ..., "units": ...}
donors = []

VALID_GROUPS = "A+, A-, B+, B-, AB+, AB-, O+, O-"


# ---------- File handling ----------
def load_donors():
    """Read donors from donors.txt into the donors list."""
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(", ")          # name, group, units
                donor = {"name": parts[0], "group": parts[1], "units": int(parts[2])}
                donors.append(donor)
        file.close()
    except FileNotFoundError:
        pass   # file does not exist yet, so start with an empty list


def save_donor(donor):
    """Add one donor line to donors.txt."""
    file = open(FILE_NAME, "a")
    file.write(donor["name"] + ", " + donor["group"] + ", " + str(donor["units"]) + "\n")
    file.close()


# ---------- Input helpers ----------
def get_blood_group():
    """Ask for blood group. Return None if it is invalid."""
    group = input("Blood group: ").strip().upper()
    if group not in stock:
        print("Invalid blood group. Valid groups: " + VALID_GROUPS + ".")
        return None
    return group


def get_units():
    """Ask for units. Return None if not a positive whole number."""
    text = input("Units: ").strip()
    if not text.isdigit() or int(text) <= 0:
        print("Invalid units. Enter a positive whole number.")
        return None
    return int(text)


# ---------- Menu features ----------
def add_donor():
    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    group = get_blood_group()
    if group is None:
        return
    units = get_units()
    if units is None:
        return

    donor = {"name": name, "group": group, "units": units}
    donors.append(donor)          # add to list
    save_donor(donor)             # save to file
    stock[group] = stock[group] + units   # update stock

    print("Donor saved to donors.txt. Stock of " + group + " is now " + str(stock[group]) + " units.")


def issue_blood():
    group = get_blood_group()
    if group is None:
        return
    units = get_units()
    if units is None:
        return

    if stock[group] < units:
        print("Insufficient stock: only " + str(stock[group]) + " unit(s) of " + group + " available.")
    else:
        stock[group] = stock[group] - units
        print(str(units) + " unit(s) of " + group + " issued. Stock of " + group + " is now " + str(stock[group]) + " units.")


def view_stock():
    print("Blood Stock:")
    for group in stock:
        print(group + ": " + str(stock[group]) + " unit(s)")


def search_donors():
    group = get_blood_group()
    if group is None:
        return

    print("Donors with blood group " + group + ":")
    count = 0
    for donor in donors:                  # linear search through the list
        if donor["group"] == group:
            count = count + 1
            print(str(count) + ". " + donor["name"] + " - " + str(donor["units"]) + " unit(s)")
    print("Total donors found: " + str(count))


# ---------- Main program ----------
def main():
    load_donors()
    while True:
        print("\n===== Blood Bank Management System =====")
        print("1. Add donor")
        print("2. Issue blood")
        print("3. View stock")
        print("4. Search donors")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_donor()
        elif choice == "2":
            issue_blood()
        elif choice == "3":
            view_stock()
        elif choice == "4":
            search_donors()
        elif choice == "5":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
