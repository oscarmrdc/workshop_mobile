

#/data/public/tools/proxys/mitmproxy-6.0.2-linux/mitmdump -s mitmproxy_cipher_dni_aburp.py --mode upstream:https://192.168.0.125:8066 --ssl-insecure --listen-port 8080

import typing
import json
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

from mitmproxy import command
from mitmproxy import ctx
from mitmproxy import flow
from mitmproxy import http



class Cifrar:
    global key
    global iv
    key = 'bf3c199c2470cb477d907b1e0917c17b'.encode()
    iv = '5183666c72eec9e4'.encode()

    def descifrar(ciphertext):
        aes = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(aes.decrypt(b64decode(ciphertext)),16)
        return plaintext.decode()

class MyAddon:

    def request(self, flow):
        if "dniv4" in flow.request.pretty_url and flow.request.method=="GET":
            #flow.request.headers["count"] = "0000"
            #headers = copy(flow.request.headers)
            #solicitud=str(flow.request.content)
            path = flow.request.path
            ctx.log.info(path)
            datoEncriptado = flow.request.path.split('/')[4]
            ctx.log.info(datoEncriptado)
            datoPlano = Cifrar.descifrar(datoEncriptado)
            ctx.log.info(datoPlano)
            flow.request.path="/api/tutorials/dniv4/"+datoPlano
            ctx.log.info("REQUEST MODIFICADO")
            

addons = [
    MyAddon()
]

