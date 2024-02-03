import os
import platform
import socket
import psutil
import wmi
from uuid import getnode
from requests import get
import ctypes


def new_function_for_screen_size():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)  # width in pixels
    height = user32.GetSystemMetrics(1)  # height in pixels
    diagonal_size = round(((width * 2 + height * 2) ** 0.5) / 25.4, 1)  # convert pixels to inches
    return f"Screen Size: {diagonal_size} inch"

def different_function_for_installed_software():
    installed_software = os.popen('wmic product get name,version').read()
    return installed_software

def another_function_for_screen_resolution():
    user32 = wmi.WMI()
    screen_resolution = user32.Win32_VideoController()[0].CurrentHorizontalResolution
    return f'Screen Resolution: {screen_resolution}'

def custom_function_for_cpu_info():
    cpu_info = platform.processor()
    cores_threads = psutil.cpu_count(logical=False), psutil.cpu_count(logical=True)
    return f'CPU Model: {cpu_info}, Cores: {cores_threads[0]}, Threads: {cores_threads[1]}'

def function_for_gpu_info():
    try:
        user32 = wmi.WMI()
        gpu_info = user32.Win32_VideoController()[0].Description
        return f'GPU Model: {gpu_info}'
    except Exception as e:
        return 'GPU Model: Not available'

def function_for_ram_size():
    ram_info = psutil.virtual_memory().total / (1024**3)  # in GB
    return f'RAM Size: {ram_info:.2f} GB'


def get_network_info_with_custom_name():
    mac_address = ':'.join(['{:02x}'.format((getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    return f'WiFi/Ethernet MAC Address: {mac_address}'

def retrieve_public_ip():
    public_ip = get('https://api64.ipify.org').text
    return f'Public IP Address: {public_ip}'

def fetch_windows_version():
    return f'Windows Version: {platform.version()}'

if __name__ == "_main_":
    print("Installed Software List:")
    print(different_function_for_installed_software())

    # print("\nInternet Speed:")
    # print(get_internet_speed())

    print("\nSystem Information:")
    print(another_function_for_screen_resolution())
    print(custom_function_for_cpu_info())
    print(function_for_gpu_info())
    print(function_for_ram_size())
    print(new_function_for_screen_size())
    print(retrieve_public_ip())
    print(fetch_windows_version())
    print(get_network_info_with_custom_name())