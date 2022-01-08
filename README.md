### Install python things
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1  # If your IDE has not to do it.
pip install -U pip
pip install -r requirements.txt
```
### Run server (python flask)
```powershell
$env:FLASK_APP = "get_hwinfo_values"
flask run
```

- run HWiNFO Portable x32 v7.16-4650 from RemoteHWInfo_v0.4 (Sensors-only mode)
- Optional: Run GPU-Z (In my case from `winget install GPU-Z` (2.41.0))
- Optional: Run Afterburner v4.6.4.16094 Beta 3 (Just install as usual)
- Optional: Run .\remotehwinfo.exe (Run as administrator)

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

### Referenses:

- https://codebeautify.org/jsonviewer
- https://github.com/iganeshk/LaMetric-System-Monitor

### Credits:

- https://github.com/Demion/remotehwinfo
- https://www.hwinfo.com/forum/threads/introducing-remote-sensor-monitor-a-restful-web-server.1025/page-4

### Changelog:

- **v0.4** - [RemoteHWInfo v0.4](https://github.com/Demion/remotehwinfo/releases/download/v0.4/RemoteHWInfo_v0.4.zip)
  - Add log file switch option.
- **v0.3** - [RemoteHWInfo v0.3](https://github.com/Demion/remotehwinfo/releases/download/v0.3/RemoteHWInfo_v0.3.zip)
  - Fix buffer overflow.
  - Update index.html format.
- **v0.2** - [RemoteHWInfo v0.2](https://github.com/Demion/remotehwinfo/releases/download/v0.2/RemoteHWInfo_v0.2.zip)
  - Add GPU-Z monitoring.
  - Add MSI Afterburner monitoring.
- **v0.1** - [RemoteHWInfo v0.1](https://github.com/Demion/remotehwinfo/releases/download/v0.1/RemoteHWInfo_v0.1.zip)

### About:

RemoteHWInfo HWiNFO / GPU-Z / MSI Afterburner Remote Monitor HTTP JSON Web Server

### Usage:

- **-port** _(60000 = default)_
- **-hwinfo** _(0 = disable; 1 = enable = default)_
- **-gpuz** _(0 = disable; 1 = enable = default)_
- **-afterburner** _(0 = disable; 1 = enable = default)_
- **-log** _(0 = disable; 1 = enable = default)_
- **-help**

* http<nolink>://ip:port/**json.json** _(UTF-8)_
  - http<nolink>://ip:port/json.json?**enable=0,1,2,3** _(0,1,2,3 = entryIndex)_
  - http<nolink>://ip:port/json.json?**disable=0,1,2,3** _(0,1,2,3 = entryIndex)_
* http<nolink>://ip:port/**index.html** _(UTF-8)_
* http<nolink>://ip:port/**404.html** _(UTF-8)_

### Credits:

- HWiNFO - Professional System Information and Diagnostics https://www.hwinfo.com/
- Remote Sensor Monitor - A RESTful Web Server (Ganesh_AT) https://www.hwinfo.com/forum/Thread-Introducing-Remote-Sensor-Monitor-A-RESTful-Web-Server
- GPU-Z - Graphics Card GPU Information Utility https://www.techpowerup.com/gpuz/
- MSI Afterburner https://www.msi.com/page/afterburner
