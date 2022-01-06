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

### Credits:
- https://github.com/Demion/remotehwinfo

### Changelog:

- **v0.4** - [RemoteHWInfo v0.4](https://github.com/Demion/remotehwinfo/releases/download/v0.4/RemoteHWInfo_v0.4.zip)
  * Add log file switch option.
- **v0.3** - [RemoteHWInfo v0.3](https://github.com/Demion/remotehwinfo/releases/download/v0.3/RemoteHWInfo_v0.3.zip)
  * Fix buffer overflow.
  * Update index.html format.
- **v0.2** - [RemoteHWInfo v0.2](https://github.com/Demion/remotehwinfo/releases/download/v0.2/RemoteHWInfo_v0.2.zip)
  * Add GPU-Z monitoring.
  * Add MSI Afterburner monitoring.
- **v0.1** - [RemoteHWInfo v0.1](https://github.com/Demion/remotehwinfo/releases/download/v0.1/RemoteHWInfo_v0.1.zip)

### About:

RemoteHWInfo HWiNFO / GPU-Z / MSI Afterburner Remote Monitor HTTP JSON Web Server

### Usage:

- **-port** *(60000 = default)*
- **-hwinfo** *(0 = disable; 1 = enable = default)*
- **-gpuz** *(0 = disable; 1 = enable = default)*
- **-afterburner** *(0 = disable; 1 = enable = default)*
- **-log** *(0 = disable; 1 = enable = default)*
- **-help**
+ http<nolink>://ip:port/**json.json** *(UTF-8)*
	+ http<nolink>://ip:port/json.json?**enable=0,1,2,3** *(0,1,2,3 = entryIndex)*
	+ http<nolink>://ip:port/json.json?**disable=0,1,2,3** *(0,1,2,3 = entryIndex)*
+ http<nolink>://ip:port/**index.html** *(UTF-8)*
+ http<nolink>://ip:port/**404.html** *(UTF-8)*

### Credits:

- HWiNFO - Professional System Information and Diagnostics https://www.hwinfo.com/
- Remote Sensor Monitor - A RESTful Web Server (Ganesh_AT) https://www.hwinfo.com/forum/Thread-Introducing-Remote-Sensor-Monitor-A-RESTful-Web-Server
- GPU-Z - Graphics Card GPU Information Utility https://www.techpowerup.com/gpuz/
- MSI Afterburner https://www.msi.com/page/afterburner