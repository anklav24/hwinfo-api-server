cd %~dp0 & python -m venv venv & ".\venv\Scripts\activate" && pip install -r requirements.txt && python hwinfo_api_server.py & deactivate < nul
