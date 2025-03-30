import tls_client

headers = {
    'authorization': 'Basic ZG1yeWZlc2NkYm90dWJldW56NXo6NU45aThPV2cyVmtNcm1oekNfNUNXekRLOG55SXo0QU0=',
    'connection': 'Keep-Alive',
    'content-type': 'application/x-www-form-urlencoded',
    'etp-anonymous-id': '71166ae5-eeb0-46a6-a320-84f90463fd1a',
    'host': 'www.crunchyroll.com',
    'user-agent': 'Crunchyroll/3.74.2 Android/15 okhttp/4.12.0',
    'x-datadog-sampling-priority': '0',
}

payload = {
    "username": "bilalxbox90@gmail.com",
    "password": "Bil@l900",
    "grant_type": "password",
    "scope": "offline_access",
    "device_id": "e80c4f4f-a2bb-40ea-87c2-41c671b7ba09",
    "device_name": "sdk_gphone64_x86_64",
    "device_type": "Google sdk_gphone64_x86_64"
}

response = tls_client.Session("okhttp4_android_13", random_tls_extension_order=True).post('https://www.crunchyroll.com/auth/v1/token',headers=headers, data=payload)

print(response.text)
print(response.status_code)