def party_invitations(names):
    # Check if the list has at least 3 names
    if len(names) < 3:
        print("Please provide at least 3 names for the party invitations.")
        return

    # Generate and print invitations using a for loop
    for name in names:
        invitation = f"Hi {name}, You're invited to my party on Friday!"
        print(invitation)

# Example usage with a list of names
names_list = ["Ryan", "James", "Osky", "Megan Dee Stallion"]
party_invitations(names_list)
