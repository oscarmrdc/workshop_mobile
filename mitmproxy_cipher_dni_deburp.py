

#/data/public/tools/proxys/mitmproxy-6.0.2-linux/mitmdump -s mitmproxy_cipher_dni_deburp.py --listen-port 8081

import typing
import json
import sys
import urllib.parse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode, urlsafe_b64encode

from mitmproxy import command
from mitmproxy import ctx
from mitmproxy import flow
from mitmproxy import http



class Cifrar:
    global key
    global iv
    key = 'bf3c199c2470cb477d907b1e0917c17b'.encode()
    iv = '5183666c72eec9e4'.encode()

    def cifrar(message):
        aes = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = aes.encrypt(pad(message.encode(),16))
        #return b64encode(ciphertext).decode()
        return urlsafe_b64encode(ciphertext).decode()

class MyAddon:

    def request(self, flow):
        if "dniv4" in flow.request.pretty_url and flow.request.method=="GET":
            #flow.request.headers["count"] = "0000"
            #headers = copy(flow.request.headers)
            #solicitud=str(flow.request.content)
            path = flow.request.path
            ctx.log.info(path)
            datoPlano = flow.request.path.split('/')[4]
            ctx.log.info(datoPlano)
            datoEncriptado = Cifrar.cifrar(datoPlano)
            ctx.log.info(datoEncriptado)
            flow.request.path="/api/tutorials/dniv4/"+datoEncriptado
            ctx.log.info("REQUEST MODIFICADO")
            

addons = [
    MyAddon()
]

