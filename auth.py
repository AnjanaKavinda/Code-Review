def login_user(username, password):
    # Missing function: get_user_by_email()
    user = get_user_by_email(username)
    if user and user["password"] == password:
        return user
    return None