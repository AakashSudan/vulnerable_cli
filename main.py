import os
import sys

GREEN = "\033[92m"
RESET = "\033[0m"

def run_brute_force():
    print(f"{GREEN}\n[+] Starting Brute Force Attack...")
    os.system('python3 brute-force/main.py')

def run_sql_injection_scanner(target_url):
    print(f"{GREEN}\n[+] Starting SQL Injection Scanner...{RESET}")
    os.system(f'python3 sql_injection_scanner/sqliv.py -t {target_url}')

def run_xss_scanner(target_url):
    print(f"{GREEN}\n[+] Starting XSS Scanner...{RESET}")
    os.system(f'python3 xss_scanner/xss_scanner.py {target_url}')

def main_menu():
    print(f"{GREEN}=================================")
    print("             Vulnerable          ")
    print(f"================================={RESET}")
    print(f"{GREEN}1. Brute Force Attack{RESET}")
    print(f"{GREEN}2. SQL Injection Scanner{RESET}")
    print(f"{GREEN}3. XSS Scanner{RESET}")
    print(f"{GREEN}4. Exit{RESET}")
    
    choice = input(f"{GREEN}\nSelect an option: {RESET}")
    
    if choice == '1':
        run_brute_force()
    elif choice == '2':
        target_url = input(f"{GREEN}\nEnter the target URL for SQL Injection Scanner: {RESET}")
        run_sql_injection_scanner(target_url)
    elif choice == '3':
        target_url = input(f"{GREEN}\nEnter the target URL for XSS Scanner: {RESET}")
        run_xss_scanner(target_url)
    elif choice == '4':
        sys.exit(f"{GREEN}\nExiting Vulnerable. Goodbye!{RESET}")
    else:
        print(f"{GREEN}\n[!] Invalid choice. Please try again.{RESET}")
        main_menu()

if __name__ == "__main__":
    while True:
        main_menu()
