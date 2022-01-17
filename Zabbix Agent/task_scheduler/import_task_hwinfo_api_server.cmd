@ECHO OFF
cd %~dp0
schtasks /Create /tn "HWiNFO API Server" /XML "Task HWiNFO API Server.xml" /F
timeout /t 5