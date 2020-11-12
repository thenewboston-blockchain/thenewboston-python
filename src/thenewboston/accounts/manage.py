from nacl.signing import SigningKey


def create_account():
    """
    Create a new account
    Return signing_key, account_number
    """

    signing_key = SigningKey.generate()
    account_number = signing_key.verify_key
    return signing_key, account_number
