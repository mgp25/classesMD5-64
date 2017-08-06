import zipfile
import hashlib
import base64

apkName = "WA.apk"
try:
    zipFile = zipfile.ZipFile(apkName,'r')
    hash = hashlib.md5()
    hash.update(zipFile.read('classes.dex'))

    print("ClassesDEX: "+ base64.b64encode(hash.digest()));
except Exception:
    print("WA.apk not found.")
