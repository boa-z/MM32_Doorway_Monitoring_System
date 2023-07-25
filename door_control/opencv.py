import cv2

def take_photo():
    # 创建一个摄像头对象，通常0代表默认摄像头，如果有多个摄像头，可以尝试其他索引。
    camera = cv2.VideoCapture(1)

    if not camera.isOpened():
        print("无法打开摄像头")
        return

    # 循环读取摄像头的帧，直到成功读取一帧
    while True:
        ret, frame = camera.read()

        if not ret:
            print("无法获取帧")
            break

        # 显示实时摄像头图像窗口，您可以调整窗口名称。
        cv2.imshow('Camera', frame)

        # 在按下 'q' 键时拍摄一张照片并退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            photo_filename = 'photo.jpg'  # 定义照片的保存文件名
            cv2.imwrite(photo_filename, frame)
            print(f"照片已保存为：{photo_filename}")
            break

    # 释放摄像头资源
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    take_photo()