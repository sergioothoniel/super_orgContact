from flask import Flask, redirect, request, jsonify, session
from flask_cors import CORS
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
CORS(app)

@app.route('/api/getdata', methods=['GET'])
def get_resource():
    return jsonify({
        "message": "Hello, Flask!",
        "status": "success",
        "data": {
            "example": "This is a simple GET response."
        }
    }), 200  


app.secret_key = os.getenv("SECRET_KEY")
SCOPES = ["https://www.googleapis.com/auth/contacts.readonly", "https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"]
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Configuração do cliente OAuth2
CLIENT_SECRETS_FILE = "credentials.json"

@app.route("/api/auth-url")
def get_auth_url():    
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )
    auth_url, _ = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )
    return jsonify({"auth_url": auth_url})


@app.route("/api/callback")
def callback():    
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )
    flow.fetch_token(authorization_response=request.url)
    creds = flow.credentials
    
    session["google_token"] = creds.token    
    return jsonify({"message": "Authentication successful", "token": creds.token})


@app.route("/api/generatetoken", methods=["POST"])
def exchange_code():
    try:        
        code = request.json.get("code")
        if not code:
            return jsonify({"error": "Authorization code is required"}), 400
        
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(code=code)
        creds = flow.credentials        
        token = creds.token
        session["google_token"] = creds.token
        return jsonify({"message": "Generate Token successful", "token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/api/contacts", methods=["POST"])
def get_contacts():
    from googleapiclient.discovery import build

    token = request.json.get("google_token")
    if not token:
        return jsonify({"error": "Unauthorized"}), 401

    creds = Credentials(token)
    service = build("people", "v1", credentials=creds)
    results = (
        service.people()
        .connections()
        .list(
            resourceName="people/me",
            pageSize=20,
            personFields="names,emailAddresses",
        )
        .execute()
    )
    
    connections = results.get("connections", [])
    return jsonify({"connections": connections})


if __name__ == '__main__':
    app.run(debug=True)