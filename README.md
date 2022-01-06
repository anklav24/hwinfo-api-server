- Copy and run HWiNFO Portable x32 v7.16-4650 from RemoteHWInfo_v0.4 (Sensors-only mode)
- Run GPU-Z (In my case from `winget install GPU-Z` (2.41.0))
- Run Afterburner v4.6.4.16094 Beta 3 (Just install as usual)
- Run .\remotehwinfo.exe (Run as administrator)
- Go to browser `http://localhost:60000/json.json`

```

enum class HwinfoReadingType
{
	None,
	Temp,
	Voltage,
	Fan,
	Current,
	Power,
	Clock,
	Usage,
	Other
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
