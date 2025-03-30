import tls_client

headers = {
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc3UGlwXy1JWTZuYkY4RmVuY18xZmciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXNfaWQiOiI3MTE2NmFlNS1lZWIwLTQ2YTYtYTMyMC04NGY5MDQ2M2ZkMWEiLCJiZW5lZml0cyI6W10sImNsaWVudF9pZCI6ImNyX2FuZHJvaWQiLCJjbGllbnRfdGFnIjoiMy43NC4yIiwiY291bnRyeSI6IkhVIiwiZGV2aWNlX2lkIjoiZDc2MzFkNWQtYjEzZi00NDc4LTkyZDctNzM2YjMxZGY0NDdjIiwiZXRwX3VzZXJfaWQiOiI2ZGM5MDc3Yi1kN2NlLTVhN2EtYjZhMS03MWU5Njc1NDQ2ZDUiLCJleHAiOjE3Mzg2MTk1MjAsImp0aSI6IjdhYzMzM2VmLWFjODEtNDk2Yy05NGE2LTVhMWRlZjMxNzAyYiIsIm1hdHVyaXR5IjoiTTIiLCJvYXV0aF9zY29wZXMiOiJhY2NvdW50OnJlYWQgY29udGVudCBtcDpsaW1pdGVkIG9mZmxpbmVfYWNjZXNzIiwicHJvZmlsZV9pZCI6IjZkYzkwNzdiLWQ3Y2UtNWE3YS1iNmExLTcxZTk2NzU0NDZkNSIsInJ0X2lkIjoiY3VnamlsNTIyY2lhNXNmcm5rMmciLCJzY29wZXMiOnsiY3IiOnsiYWNjX2lkIjoiNmRjOTA3N2ItZDdjZS01YTdhLWI2YTEtNzFlOTY3NTQ0NmQ1IiwiZXh0X2lkIjoiMTEyODIzNjU2MiJ9fSwic3RhdHVzIjoiQUNUSVZFIiwidG50IjoiY3IifQ.Lrxsv2cchWcpdyij-RPq2SGRjHRl7CXJ6xqtrwdz27hOmkNaFYuIPPXEn2_W8z3sm00x1ZqICYtGJuiO9wGmeGYwPgcxiBvU6g9KVGTnk9k0tFCvyVHTWq_SeBNwk3s0sB9xTMAhM3LcqHRLWdJ41jx-ynvmicJHut6LIS3ePpDpDDPs4L3ZW0ecnPxoJb0Z8F38EyZb-kj5Fd26dZx8pBvVhjbVwlGiXKDZSkbzaISuUQ8Z1zBnl11jp-wLFa-RBltJD0eGbRUMmvBIydzSkVidZYkLw9Njz0ohs7AwbB7uNiJNni1eFj7Jc8VLl90WF6Bftp9LHUiakzphV8FCnA',
    'connection': 'Keep-Alive',
    'etp-anonymous-id': '64c60faa-957c-4b53-b519-80845ceb1f38',
    'host': 'www.crunchyroll.com',
    'if-modified-since': 'Mon, 03 Feb 2025 18:30:01 GMT',
    'user-agent': 'Crunchyroll/3.74.2 Android/15 okhttp/4.12.0',
    'x-datadog-sampling-priority': '0',
}

response = tls_client.Session("okhttp4_android_13", random_tls_extension_order=True).get('https://www.crunchyroll.com/subs/v1/subscriptions/1128236562/benefits', headers=headers)

print(response.text)
print(response.status_code)