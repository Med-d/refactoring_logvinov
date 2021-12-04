from PIL import Image
import numpy as np


def graying_image(img,
                  step,
                  graduation,
                  res_name):
    arr = np.array(img)
    row_count = len(arr)
    col_count = len(arr[1])
    i = 0
    while i <= row_count - step:
        j = 0
        while j <= col_count - step:
            s = 0
            for row in range(i, i + step):
                for col in range(j, j + step):
                    r = int(arr[row][col][0] / 3)
                    g = int(arr[row][col][1] / 3)
                    b = int(arr[row][col][2] / 3)
                    M = r + g + b
                    s += M
            s = int(s // step ** 2)
            for row in range(i, i + step):
                for col in range(j, j + step):
                    arr[row][col][0] = int(s // graduation) * graduation
                    arr[row][col][1] = int(s // graduation) * graduation
                    arr[row][col][2] = int(s // graduation) * graduation
            j = j + step
        i = i + step
    Image.fromarray(arr).save(res_name + '.jpg')


def input_data():
    print("Введите название файла изображения:", end=" ")
    img = Image.open(input())
    print("Введите шаг:", end=" ")
    step = int(input())
    print("Введите кколичество градаций серого:", end=" ")
    graduation = 255 // int(input())
    print("Введите имя результирующего изображения (без расширения):")
    res_name = input()
    return img, step, graduation, res_name


img, step, graduation, res_name = input_data()
graying_image(img, step, graduation, res_name)
