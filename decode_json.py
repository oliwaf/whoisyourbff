import re
from functools import partial
import json



fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m.group(1).decode()))

path = r'C:\Users\Kacper\IdeaProjects\NoweRzeczy'

with open('message_1.json', 'rb') as binary_data:
    repaired = fix_mojibake_escapes(binary_data.read())
data = json.loads(repaired.decode('utf8'))



