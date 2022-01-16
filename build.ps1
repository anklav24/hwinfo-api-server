rm -Recurse -Force .\dist\
rm -Recurse -Force .\build\

pyinstaller.exe --onefile hwinfo_api_server.py --add-data "api/templates;api/templates" --add-data "api/static;api/static" --add-data "api/third_party;api/third_party"
xcopy  api\third_party\* dist\api\third_party\* /E/Y
xcopy  zabbix_agentd.conf.d\* zabbix_agentd.conf.d\* /E/Y

rm -Recurse -Force .\build\
rm -Recurse -Force .\dist\api\third_party\process_control.py
