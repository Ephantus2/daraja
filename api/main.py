from fastapi import FastAPI

app = FastAPI()

@app.get("api/")
def get_token():
    consumer_key = "eSQFZduKSQDj680euPXR4huvjcpfYJkWsbAK6T4dOAVsTNA8"
    consumer_secret = "pBPwGPOxtmB9fvu8vhc1Y4slVZAuG5ROgKPys9GrhKLcw9iGGcs77xpFJYLRM3nM"
    
    
    auth_string = f"{consumer_key}: {consumer_secret}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()
    
    try:
        
    except:
        print("an error occured")