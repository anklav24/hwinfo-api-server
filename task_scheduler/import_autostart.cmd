@ECHO OFF
cd %~dp0
schtasks /Create /tn "HWiNFO API Server" /XML "HWiNFO API Server.xml" /F
timeout /t 5