import ctypes
import ctypes.util
import socket
import subprocess

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

def mount(path_to_smb, path_to_local_dir):
    retcode = subprocess.call(["/usr/bin/mount", "-t", "cifs", "-o", "uid=1000,gid=1000,credentials=/home/monica/.smbcredentials", path_to_smb, path_to_local_dir])

localIP = socket.gethostbyname(socket.gethostname())

if("10.0.0." in localIP):
    #Usage: mount('remote directory', 'local directory')
    mount('//10.0.0.6/Plex', '/mnt/Plex')
    mount('//10.0.0.6/monica', '/mnt/home')
elif("192.168.68." in localIP):
    #Usage: mount('remote directory', 'local directory')
    mount('//192.168.68.11/Games', '/mnt/Games')
    mount('//192.168.68.11/monica', '/mnt/home')
