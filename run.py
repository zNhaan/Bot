import os
import time

if __name__ == "__main__":
    with open("config.txt", "r") as file:
        config = file.read().strip()  # Thêm .strip() để loại bỏ khoảng trắng thừa
    command = f"java -jar mc-bots-1.2.11.jar -s {config} -r -ar 1"
    while True:
        os.system(command)
        time.sleep(1)
