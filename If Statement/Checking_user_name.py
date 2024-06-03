current_users = ['LEMI', 'kiya', 'umeran', 'beki', 'sifen']
new_users = ['nati', 'lemi', 'beki', 'kenean']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry this user name is not available.")
    else:
        print("Available.")