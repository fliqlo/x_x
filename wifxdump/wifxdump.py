import os
import subprocess

def get_wifi_passwords():
    # Get list of all saved Wi-Fi profiles
    command = "netsh wlan show profiles"
    profiles_output = subprocess.check_output(command, shell=True).decode('utf-8')
    
    # Extract SSIDs
    ssids = []
    for line in profiles_output.split('\n'):
        if "All User Profile" in line:
            ssid = line.split(":")[1].strip()
            ssids.append(ssid)

    # Get password for each SSID
    for ssid in ssids:
        # The 'key=clear' argument displays the clear-text password
        command = f'netsh wlan show profile name="{ssid}" key=clear'
        profile_info = subprocess.check_output(command, shell=True).decode('utf-8')
        
        # Extract the password line
        for line in profile_info.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                print(f"SSID: {ssid} | Password: {password}")
                break

if __name__ == "__main__":
    get_wifi_passwords()