USER_TOKENS = {}

def set_user_token(username, jti):
    print(f'setting jti- {jti} for user- {username}')
    USER_TOKENS[username] = jti

def get_user_token(username):
    jti = USER_TOKENS.get(username)
    print(f'getting jti- {jti} for user- {username}')
    return jti
