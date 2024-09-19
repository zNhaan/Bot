import os

if __name__ == "__main__":
  with open("config.txt" , "r") as file:
    config = file.read()
  while True:
    os.system(f"java -jar mc-bots-1.2.11.jar -s {config} -r -ar 1")
