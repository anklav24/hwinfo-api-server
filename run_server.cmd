cd %~dp0 && python -m venv venv && ".\venv\Scripts\activate" && pip install -r requirements.txt && python get_hwinfo_values.py & deactivate < nul
