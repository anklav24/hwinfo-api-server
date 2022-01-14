import os
import subprocess


def run_processes(remote_hwinfo_port: int) -> None:
    os.startfile(r'api\third_party\HWiNFO32.exe', show_cmd=False)
    os.startfile(r'api\third_party\remotehwinfo.exe',
                 arguments=f"-port {remote_hwinfo_port} -log 0 -hwinfo 1 -gpuz 0 -afterburner 0",
                 show_cmd=False)
    subprocess.run('tasklist /fi "imagename eq HWiNFO32.exe"')
    subprocess.run('tasklist /fi "imagename eq remotehwinfo.exe"')
    print()


def kill_processes() -> None:
    os.system("taskkill /f /im remotehwinfo.exe")
    os.system("taskkill /f /im HWiNFO32.exe")
