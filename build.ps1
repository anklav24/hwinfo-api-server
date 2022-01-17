taskkill /f /im remotehwinfo.exe
taskkill /f /im HWiNFO32.exe

rm -Recurse -Force .\hwinfo_api_server\
rm -Recurse -Force .\build\

pyinstaller.exe --onefile hwinfo_api_server.py --distpath hwinfo_api_server --add-data "api/templates;api/templates" --add-data "api/static;api/static" --add-data "api/third_party;api/third_party"
xcopy  api\third_party\* hwinfo_api_server\api\third_party\* /E/Y
xcopy  zabbix_agentd.conf.d\* hwinfo_api_server\zabbix_agentd.conf.d\* /E/Y
xcopy  tests\* hwinfo_api_server\tests\* /E/Y
cp .\README.md .\hwinfo_api_server\

rm -Recurse -Force .\build\
rm -Recurse -Force .\hwinfo_api_server\api\third_party\process_control.py
rm -Recurse -Force hwinfo_api_server.spec