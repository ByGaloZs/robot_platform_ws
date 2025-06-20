import requests

BASE_URL = "http://localhost:8000"

def send_command(command):
    url = f"{BASE_URL}/{command}"
    response = requests.get(url)
    print(f"Respuesta [{command}]:", response.json())

if __name__ == "__main__":
    send_command("start")
    send_command("status")
    send_command("stop")
