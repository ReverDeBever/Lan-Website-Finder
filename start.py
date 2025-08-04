import requests # Web requests
import webbrowser # O urls in browser
from concurrent.futures import ThreadPoolExecutor # Parallel execution for faster scanning

# Variables

base_ip = "192.168.2."
ports = [80, 443,]
timeout = 2
found_websites = []

def check_website(ip): # Function to check if a website is available on a given local ip
    global found_websites
    for port in ports:
        protocol = "https" if port == 443 else "http" # Determine protocol based on port
        url = f"{protocol}://{ip}" # Construct the URL
        try:
            response = requests.get(url, timeout=timeout, verify=False) # Send a GET request to the URL
            if response.status_code < 400: # Check if the response status code indicates success
                print(f"Website found: {url}") # Print the found website
                found_websites.append(url) # Add the website to the list of found websites
                return
        except requests.RequestException: # Handle any request exceptions
            pass 
def scan_network(): # Function to scan the local network for websites
    print("Scanning network") # Print a message indicating the start of the scan
    with ThreadPoolExecutor(max_workers = 50) as executor: # Use a thread pool for parallel execution
        for i in range(1, 255): # Iterate over the last octet of the IP address
            ip = f"{base_ip}{i}"
            executor.submit(check_website, ip) 

    if found_websites: # Check if any websites were found
        print(f"\nOpening {len(found_websites)} site(s) in browser:")
        for site in found_websites:
            webbrowser.open(site) # Open each found website in the default web browser
    else:
        print("No websites found on the local network.")

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings() # Disable SSL warnings
    scan_network() # Start the network scan