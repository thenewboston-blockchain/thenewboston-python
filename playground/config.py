import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOCKS_DIR = os.path.join(BASE_DIR, 'blocks')
SIGNED_REQUESTS_DIR = os.path.join(BASE_DIR, 'signed_requests')
SIGNING_KEY_DIR = os.path.join(BASE_DIR, 'signing_keys')

# Account numbers
BANK_ACCOUNT_NUMBER = '5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8'
BANK_NID_ACCOUNT_NUMBER = 'd5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1'
BUCKY_ACCOUNT_NUMBER = '484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc'
CHRISTOPHER_ACCOUNT_NUMBER = 'a29baa6ba36f6db707f8f8dacfa82d5e8a28fa616e8cc96cf6d7790f551d79f2'
JUSTIN_ACCOUNT_NUMBER = '3214108063cda7b259782c57ff8cec343ad2f1ad35baf38c3503db5cf6f3b2f7'
KRISTY_ACCOUNT_NUMBER = 'db1a9ac3c356ab744ab4ad5256bb86c2f6dfaa7c1aece1f026a08dbd8c7178f2'
TREASURY_ACCOUNT_NUMBER = '0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb'
VALIDATOR_ACCOUNT_NUMBER = 'ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314'
VALIDATOR_NID_ACCOUNT_NUMBER = '3afdf37573f1a511def0bd85553404b7091a76bcd79cdcebba1310527b167521'

# Bank fees
BANK_REGISTRATION_FEE = 2
BANK_TX_FEE = 1

# Validator fees
VALIDATOR_REGISTRATION_FEE = 8
VALIDATOR_TX_FEE = 4
