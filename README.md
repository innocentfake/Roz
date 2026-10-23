# For Roz — A Quiet Constellation

A small, literary, dark-themed Streamlit website inspired by roses, moonlight, and classic literature.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy online

### Streamlit Community Cloud
1. Upload `app.py`, `requirements.txt`, and this README to a **new GitHub repository**.
2. Go to https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select your repository and branch, and set the main file path to `app.py`.
4. Deploy. Streamlit will provide a public URL.

### Render
1. Create a new GitHub repository and upload these files.
2. In https://render.com/, choose **New + → Web Service** and connect the repository.
3. Use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Deploy.

## Notes
- This is a tribute-style website, not an impersonation of Roz.
- The letter area is a session-only demo. It does not send or publish letters.
- Do not add private messages, personal photos, or identifying information without permission.
