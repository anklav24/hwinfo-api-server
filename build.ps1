taskkill /f /im remotehwinfo.exe
taskkill /f /im HWiNFO32.exe

rm -Recurse -Force "Zabbix Agent\user_scripts\hwinfo_api_server\"
rm -Recurse -Force .\build\

pyinstaller.exe --onefile hwinfo_api_server.py --distpath "Zabbix Agent\user_scripts\hwinfo_api_server" --add-data "api/templates;api/templates" --add-data "api/static;api/static" --add-data "api/third_party;api/third_party"
xcopy api\third_party\* "Zabbix Agent\user_scripts\hwinfo_api_server\api\third_party\*" /E/Y
xcopy tests\* "Zabbix Agent\user_scripts\hwinfo_api_server\tests\*" /E/Y

cp .\README.md "Zabbix Agent\user_scripts\hwinfo_api_server\README.md"

rm -Recurse -Force "Zabbix Agent\user_scripts\hwinfo_api_server\api\third_party\process_control.py"
rm -Recurse -Force .\build\
rm -Recurse -Force hwinfo_api_server.spec