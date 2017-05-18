# -*- coding: utf-8 -*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from blockchain import implement
class Member(implement.Member):
    #未來拿掉
    private=""
    publics=dict()
    def __init__(self):
        pass
    def signUp(self,userName,userInfo):
        ramdom_generator = Random.new().read
        rsa = RSA.generate(1024, ramdom_generator)
        self.private_pem = rsa.exportKey()
        Member.private=self
        self.publick_pem = rsa.publickey().exportKey()
        self.userName=userName
        Member.publics[userName]=self.publick_pem
    @staticmethod
    def encrypto(userName,message):
        rsakey = RSA.importKey(Member.publics[userName])
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message))
        return cipher_text

    def decrypto(self,cipher_message):
        rsakey = RSA.importKey(self.private_pem)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        ramdom_generator = Random.new().read
        text = cipher.decrypt(base64.b64decode(cipher_message),ramdom_generator)
        return text
    
    def sign(self,message):
        rsakey = RSA.importKey(self.private_pem)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message)
        sign = signer.sign(digest)
        sign_message = base64.b64encode(sign)
        return sign_message

    @staticmethod
    def verdify(userName,message,sign_message):
        rsakey = RSA.importKey(Member.publics[userName])
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message)
        is_verify = verifier.verify(digest, base64.b64decode(sign_message))
        return is_verify
    
    def getMemberPublicKey(userName):
        rsakey = RSA.importKey(Member.publics[userName])