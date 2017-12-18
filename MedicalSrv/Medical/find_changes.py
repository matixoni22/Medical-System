import os
import cv2
import numpy as np
from .models import *
from django.core.files import File


def GenerateMask(img='', low_red1=np.array([0, 0, 0]), high_red1=np.array([0, 0, 0]), low_red2=np.array([0, 0, 0]), high_red2=np.array([0, 0, 0])):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask1 = cv2.inRange(img_hsv, low_red1, high_red1)
    img_mask2 = cv2.inRange(img_hsv, low_red2, high_red2)

    mask = cv2.bitwise_or(img_mask1, img_mask2)
    return mask


def ReturnChanges(imageid_1=0, imageid_2=0):
    img1db = Photography.objects.get(pk=imageid_1)
    img2db = Photography.objects.get(pk=imageid_2)
    file_dri = '/home/matixoni/Medical System/Server/MedicalSrv/Medical/media/images/'
    img1 = cv2.imread(file_dri + img1db.Name)
    img2 = cv2.imread(file_dri + img2db.Name)

    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]

    img_low_red1 = np.array([0, 70, 70])
    img_high_red1 = np.array([10, 255, 255])

    img_low_red2 = np.array([170, 70, 70])
    img_high_red2 = np.array([180, 255, 255])

    mask1 = GenerateMask(img1, img_low_red1, img_high_red1,
                         img_low_red2, img_high_red2)
    mask2 = GenerateMask(img2, img_low_red1, img_high_red1,
                         img_low_red2, img_high_red2)

    diff_mask = cv2.bitwise_xor(mask1, mask2)
    diff_mask_inv = cv2.bitwise_not(diff_mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=diff_mask_inv)
    b, g, r = cv2.split(img2)

    imgfg = cv2.merge((b, g, r * 0))

    img2_fg = cv2.bitwise_and(imgfg, imgfg, mask=diff_mask)
    result_img = cv2.add(img1_bg, img2_fg)

    filename = "images_ids_" + str(img1db.Id) + "-" + str(img2db.Id) + ".jpg"
    save_dir = '/home/matixoni/Medical System/Server/MedicalSrv/Medical/media/' + filename

    cv2.imwrite(save_dir, result_img)

    result = Result()
    with open(save_dir, 'rb') as doc_file:
        res = Result.objects.select_related().filter(Visit=img1db.Visit.pk)
        if res is not None:
            try:
                res[0].Image.delete(save=True)
            except Exception:
                pass
            res[0].Image.save(filename, File(doc_file), save=True)
            res[0].save()
        else:
            result.Visit = img1db.Visit
            result.Image.save(filename, File(doc_file), save=True)
            result.save()

    os.remove(save_dir)
