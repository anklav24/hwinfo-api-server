import os
import subprocess
import time


def print_waiting(sec: int) -> None:
    print("Waiting", end='')
    for _ in range(1, sec + 1):
        time.sleep(1)
        print('.', end='')
    print()


def run_processes(remote_hwinfo_port: int) -> None:
    os.startfile(r'api\third_party\HWiNFO32.exe', show_cmd=False)
    os.startfile(r'api\third_party\remotehwinfo.exe',
                 arguments=f"-port {remote_hwinfo_port} -log 0 -hwinfo 1 -gpuz 0 -afterburner 0",
                 show_cmd=False)
    subprocess.run('tasklist /fi "imagename eq HWiNFO32.exe"')
    subprocess.run('tasklist /fi "imagename eq remotehwinfo.exe"')
    print_waiting(15)


def kill_processes() -> None:
    os.system("taskkill /f /im remotehwinfo.exe")
    os.system("taskkill /f /im HWiNFO32.exe")
    print_waiting(3)
