import cv2
import matplotlib.pyplot as plt
path = "TEST.png"


model = input("Choose the model you want to use: ")
scale = int(input("Enter the scale you want to use: "))


def edsr(img_path, scale):
    img = cv2.imread(img_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = f"EDSR_x{scale}.pb"
    sr.readModel(path)
    sr.setModel("edsr", scale)
    result = sr.upsample(img)

    # Resized image
    resized = cv2.resize(img, dsize=None, fx=scale, fy=scale)
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    # Original image
    plt.imshow(img[:, :, ::-1])
    plt.subplot(1, 3, 2)
    # SR upscaled
    plt.imshow(result[:, :, ::-1])
    plt.subplot(1, 3, 3)
    # OpenCV upscaled
    plt.imshow(resized[:, :, ::-1])
    plt.show()
    return result


def espcn(img_path, scale):
    img = cv2.imread(img_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = f"ESPCN_x{scale}.pb"
    sr.readModel(path)
    sr.setModel("espcn", scale)
    result = sr.upsample(img)
    # Resized image
    resized = cv2.resize(img, dsize=None, fx=scale, fy=scale)
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    # Original image
    plt.imshow(img[:, :, ::-1])
    plt.subplot(1, 3, 2)
    # SR upscaled
    plt.imshow(result[:, :, ::-1])
    plt.subplot(1, 3, 3)
    # OpenCV upscaled
    plt.imshow(resized[:, :, ::-1])
    plt.show()


def fsrcnn(img_path, scale):
    img = cv2.imread(img_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = f"FSRCNN_x{scale}.pb"
    sr.readModel(path)
    sr.setModel("fsrcnn", scale)
    result = sr.upsample(img)
    # Resized image
    resized = cv2.resize(img, dsize=None, fx=scale, fy=scale)
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    # Original image
    plt.imshow(img[:, :, ::-1])
    plt.subplot(1, 3, 2)
    # SR upscaled
    plt.imshow(result[:, :, ::-1])
    plt.subplot(1, 3, 3)
    # OpenCV upscaled
    plt.imshow(resized[:, :, ::-1])
    plt.show()


def lapSRN(img_path, scale):
    img = cv2.imread(img_path)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = f"LapSRN_x{scale}.pb"
    sr.readModel(path)
    sr.setModel("lapsrn", scale)
    result = sr.upsample(img)
    # Resized image
    resized = cv2.resize(img, dsize=None, fx=scale, fy=scale)
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    # Original image
    plt.imshow(img[:, :, ::-1])
    plt.subplot(1, 3, 2)
    # SR upscaled
    plt.imshow(result[:, :, ::-1])
    plt.subplot(1, 3, 3)
    # OpenCV upscaled
    plt.imshow(resized[:, :, ::-1])
    plt.show()


if model == "EDSR":
    edsr(path, scale)
elif model == "ESPCN":
    espcn(path, scale)
elif model == "LapSRN":
    lapSRN(path, scale)
elif model == "FSRCNN":
    fsrcnn(path, scale)
else:
    print("Please, choose the appropriate model name")