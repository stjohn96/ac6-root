from requests import Session, ConnectionError
import hashlib

# Router IP
IP = "192.168.0.1"

# Router Password
PASS = ""

PASS_HASH = hashlib.md5(PASS.encode()).hexdigest()

HEADERS = {
    "Host": IP,
    "User-Agent": "User-Agent: Mozilla/5.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": f"http://{IP}/login.html",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "close"
}


def main():
    session = Session()

    # Force Logout
    session.get(
        f"http://{IP}/goform/exit"
    )

    # Auth
    session.post(
        f"http://{IP}/login/Auth",
        headers=HEADERS,
        data={
            'username': 'admin',
            'password': f'{PASS_HASH}'
        }
    )

    # Enable Telnet   
    try:
        session.get(
            f"http://{IP}/goform/telnet",
            headers=HEADERS
        )
    except ConnectionError as e:
        if "load telnetd success" in str(e):
            print("Telnetd Enabled")
            print("Username: root")
            print("Password: Fireitup")


if __name__ == "__main__":
    main()
