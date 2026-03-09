from tinydb import TinyDB, Query

# Memory database
db = TinyDB('memory.json')

def check_memory(error_signature):
    Error = Query()
    result = db.search(Error.signature == error_signature)
    return result[0]['fix'] if result else None

def save_fix(error_signature, fix_text):
    db.insert({'signature': error_signature, 'fix': fix_text})