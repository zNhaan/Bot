#!/bin/bash

# Đọc nội dung từ file config.txt
config=$(cat config.txt | xargs)  # xargs dùng để loại bỏ khoảng trắng thừa

# Câu lệnh java cần chạy
command="java -jar mc-bots-1.2.11.jar -s ${config} -r -ar 1"

# Vòng lặp vô hạn để thực hiện câu lệnh liên tục
while true; do
    $command
    sleep 1
done

