import numpy as np
import cv2

im = cv2.imread('GUVSimul_vP0.577_29uLens.tif',0)
# cv2.imshow('test',im)
# cv2.waitKey(0)
h, w = im.shape
ch, cw = h//2, w//2

left  = im[:, :cw]
right = im[:, cw:]
top = im[:ch, :]
bot = im[ch:, :]

diff_left_right = cv2.subtract(left, np.flip(right, axis=1))
cv2.imwrite('diff_left_right.png', diff_left_right)
diff_top_bot = cv2.subtract(top, np.flip(bot, axis=0))
cv2.imwrite('diff_top_bot.png', diff_top_bot)

max = np.amax(diff_top_bot)
print(max)
min = np.amin(diff_top_bot)
print(min)

max = np.max(diff_top_bot)
idx = np.where(diff_top_bot == max)
print("Elements with value ", max, " exists at following indices\n", idx[0])

diff_top_bot_enhanced = diff_top_bot * 200
cv2.imwrite('diff_top_bot_enhanced.png', diff_top_bot_enhanced)