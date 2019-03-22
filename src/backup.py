import logg
import sys

logg.log_file[0] = "backup_temp.log"
logg.check_logg()
backup_ext = "backup"
def backup(berkas):
    with open(berkas, "rb") as baca:
        baca = baca.read()
        
