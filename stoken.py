from itsdangerous import URLSafeTimedSerializer   
from key import salt
def encode(data):
    serailizer= URLSafeTimedSerializer('code@123')  ## creating obj   URLSAFED IS CLASS ,code@123 is any value we must insert int quotations
    return serailizer.dumps(data,salt=salt)    #we must not [push] salt key to github
def decode(data):
    serailizer= URLSafeTimedSerializer('code@123') 
    return serailizer.loads(data,salt=salt)          ##########for decoding  