# HWiFO API Server for Zabbix LLD

### Overview

- If you want to grab some data from HWiNFO, GPU-Z, Afterburner into Zabbix (LLD, HTTP Agent, Zabbix Agent)
- Based on RemoteHWInfo HWiNFO / GPU-Z / MSI Afterburner Remote Monitor HTTP JSON Web Server

### Installation

- Install Python above 3.10
- Add python path to Environment Variables (User and system variables)
- restart powershell

### Optional

- Optional: Run GPU-Z (In my case from `winget install GPU-Z` (2.41.0))
- Optional: Run Afterburner v4.6.4.16094 Beta 3 (Just install as usual)
- Optional: Run .\remotehwinfo.exe (Run as administrator)

### Run web-server

```powershell or cmd
.\run_server.cmd (Run as administrator)
```

### Links

- python flask server
  - http://localhost:50000/site-map (To get info about all methods)

### Troubleshooting:
- If `remotehwinfo.exe` shows and just disappear try to change ports
- run tests ` python -m pytest -v -s`

### References:

- https://codebeautify.org/jsonviewer
- [iganeshk / LaMetric-System-Monitor](https://github.com/iganeshk/LaMetric-System-Monitor)

### Credits:

- [Demion / remotehwinfo](https://github.com/Demion/remotehwinfo)
- [Remote Sensor Monitor - A RESTful Web Server](https://www.hwinfo.com/forum/threads/introducing-remote-sensor-monitor-a-restful-web-server.1025/)

### Credits:

- [HWiNFO - Professional System Information and Diagnostics](https://www.hwinfo.com/)
- [GPU-Z - Graphics Card GPU Information Utility](https://www.techpowerup.com/gpuz/)
- [MSI Afterburner](https://www.msi.com/page/afterburner)
