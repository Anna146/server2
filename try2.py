import cv2
import tesseract
gray = cv2.imread('13.jpg')
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
cv2.threshold(gray, 231, 255, cv2.THRESH_BINARY)
api = tesseract.tessbaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
tesseract.SetCvImage(gray,api)
print(api.GetUTF8Text())