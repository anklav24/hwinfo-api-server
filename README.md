### Overview

- If you want to grab some data from HWiNFO, GPU-Z, Afterburner into Zabbix (LLD, HTTP Agent, Zabbix Agent)

### Installation

- Install Python
- Add python.exe to Environment Variables

### Optional

- Optional: Run GPU-Z (In my case from `winget install GPU-Z` (2.41.0))
- Optional: Run Afterburner v4.6.4.16094 Beta 3 (Just install as usual)
- Optional: Run .\remotehwinfo.exe (Run as administrator)

### Run web-server

```powershell or cmd
.\run_server.cmd (Run as administrator)
```

### Links

- http://localhost:60000
- http://localhost:60000/json.json
- http://localhost:50000/values
- http://localhost:50000/hardware

```
enum class HwinfoReadingType
{
	None, 0
	Temp, 1 
	Voltage, 2 
	Fan, 3 
	Current, 4 
	Power, 5 
	Clock, 6
	Usage, 7
	Other 8
};
```

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
