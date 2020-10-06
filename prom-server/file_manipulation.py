from os import path
import io
class File():
  def __init__(self, file_dir):
    self._file_dir = file_dir
  def is_file(self):
    return path.isfile(self._file_dir)
  def open_file(self):
    with open(self._file_dir, "r") as data_file:
      return data_file.read()
  def write_to_file(self, content):
    with io.open(self._file_dir, "w+") as outfile:
      outfile.write(content)