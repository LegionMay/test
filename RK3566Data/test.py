import cv2

# 打开video9设备
cap = cv2.VideoCapture('/dev/video9', cv2.CAP_V4L2)
if not cap.isOpened():
    print("无法打开视频设备")
    exit()

# 设置捕获参数
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    # 捕获视频帧
    ret, frame = cap.read()
    if not ret:
        print("捕获到空帧")
        break

    # 使用 OpenCV 的 resize 函数来放大图像
    resized_frame = cv2.resize(frame, (600, 750))

    # 顺时针旋转90度
    rotated_frame = cv2.rotate(resized_frame, cv2.ROTATE_90_CLOCKWISE)

    # 显示旋转后的图像
    cv2.imshow('Rotated Frame', rotated_frame)

    # 等待1ms，检查是否有按键事件
    if cv2.waitKey(1) >= 0:
        break

cap.release()
 cv2.destroyAllWindows() # 如果您取消注释imshow，也应该取消注释这行代码
