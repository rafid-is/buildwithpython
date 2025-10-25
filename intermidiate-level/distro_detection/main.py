import os
import re

def get_distro_info():
    
    distro_info = {}
    os_release_path = '/etc/os-release'  # getting info from etc/os-release
    if os.path.exists(os_release_path):
        with open(os_release_path, 'r') as f:
            for line in f:
                # Match key=value pairs, handling quoted values
                match = re.match(r'^([A-Z_]+)="?(.*)"?$', line.strip())
                if match:
                    key, value = match.groups()
                    distro_info[key] = value.strip('"')
    else:
        raise FileNotFoundError("This system does not have /etc/os-release; may not be Linux or unsupported distro.")

    return distro_info


if __name__ == "__main__":
    try:
        info = get_distro_info()
        print(f"Distro: {info.get('ID', 'Unknown')}")
        print(f"Version: {info.get('VERSION_ID', 'Unknown')}")
        print(f"Pretty Name: {info.get('PRETTY_NAME', 'Unknown')}")
    except Exception as e:
        print(f"Error detecting distro: {e}")
