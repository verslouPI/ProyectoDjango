from random import randint
from uuid import uuid4
import os

def path_file_name(dir):
    def _return_function(instance, filename):
        filename, ext = os.path.splitext(filename)
        return "%s/%s%s" % (dir, uuid4(), ext)
    return _return_function


def generate_uuid():
  """
    Generate an uuid char(8)

    return str
  """
  FIRST_FIVE_NUMBERS = randint(65536, 1048575)
  OTHERS_NUMBERS = randint(256, 4095) #for more random
  UUID = hex(FIRST_FIVE_NUMBERS) + "-" + hex(OTHERS_NUMBERS)
  return UUID.replace("0x","")