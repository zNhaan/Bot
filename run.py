import os , time

if __name__ == "__main__":
  with open("config.txt" , "r") as file:
    config = file.read()
  os = f"java -jar mc-bots-1.2.11.jar -s {config} -r -ar 1"
  while True:
    os.system(os)
    sleep(1)
