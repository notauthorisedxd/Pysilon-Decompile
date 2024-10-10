import os
import sys
import time
import subprocess
import re
import base64
import marshal
import shutil  # Import shutil to handle folder deletion
from colorama import Fore, Style, init

init(autoreset=True)
DISCORD_TOKEN_REGEX = re.compile(r'^(?:(M|m)T|[A-Za-z0-9]{24}\.[A-Za-z0-9]{6}\.[A-Za-z0-9_-]{27})$')

def extract_bytecode_from_pyc(pyc_file):
    try:
        with open(pyc_file, 'rb') as f:
            header_size = 16 if sys.version_info >= (3, 6) else 8
            f.read(header_size)

            code_obj = marshal.load(f)
            return code_obj
    except Exception as e:
        print(f"{Fore.RED}[-] Error extracting bytecode from {pyc_file}: {e}{Style.RESET_ALL}")
        return None

def decode_base64_and_check_token(constant):
    try:
        decoded_token = base64.b64decode(constant[::-1]).decode()
        if len(decoded_token) > 70:
            return decoded_token
    except Exception as e:
        pass
    return None

def generate_script_template(code_obj):
    try:
        if not code_obj:
            raise ValueError("Invalid code object provided.")

        print(f"\n[+] Checking for Discord tokens in bytecode...")

        constants = code_obj.co_consts

        for const in constants:
            if isinstance(const, str):
                token = decode_base64_and_check_token(const)
                if token:
                    return token

    except Exception as e:
        print(f"{Fore.RED}[-] Error generating script template: {e}{Style.RESET_ALL}")
    return None

def decompile_exe(exe_file):
    try:
        output_dir = './'
        print(f"Starting to decrypt...")
        pyinstxtractor_path = os.path.join('utils', 'pyinstxtractor.py')

        subprocess.run(['python', pyinstxtractor_path, exe_file], check=True)
        print(f"[+] Decompiled {exe_file} to {output_dir}")

        return output_dir
    except Exception as e:
        print(Fore.RED + f"[-] Error decompiling {exe_file}: {e}" + Style.RESET_ALL)
        return None

def find_extracted_folder(base_dir):
    for entry in os.listdir(base_dir):
        if entry.endswith('_extracted') and os.path.isdir(os.path.join(base_dir, entry)):
            return os.path.join(base_dir, entry)
    return None

def delete_extracted_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"[+] Deleted extracted folder: {folder_path}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error deleting extracted folder: {e}{Style.RESET_ALL}")

def main():
    exe_file = input("Please enter the path to the .exe file: ")

    output_dir = decompile_exe(exe_file)

    if output_dir:
        time.sleep(0.5)

        extracted_folder = find_extracted_folder(output_dir)
        if extracted_folder:
            print(f"[+] Located extracted folder: {extracted_folder}")

            pyc_file_path = os.path.join(extracted_folder, 'source_prepared.pyc')
            if os.path.exists(pyc_file_path):
                print("[+] Located source_prepared.pyc")

                code_obj = extract_bytecode_from_pyc(pyc_file_path)

                if code_obj:
                    token = generate_script_template(code_obj)
                    if token:
                        print(f"{Fore.GREEN}[+] Found Discord token: {token}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}[-] No Discord token found.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] source_prepared.pyc not found in the extracted folder.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] No extracted folder found.{Style.RESET_ALL}")
        
        # After processing, delete the extracted folder
        if extracted_folder:  # Only delete if it was found
            delete_extracted_folder(extracted_folder)

if __name__ == "__main__":
    main()