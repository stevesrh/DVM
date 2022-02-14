import os
import random



video_fg_all_names=os.listdir("test_v_fg_path")
image_fg_all_names=os.listdir("test_i_fg_path")
bg_all_names=os.listdir("test_bg_path")

# 测试集
# fg_names=video_fg_all_names+image_fg_all_names
# 训练集
# fg_all_names=video_fg_all_names+random.sample(image_fg_all_names,325)
# 测试集
bg_names=random.sample(bg_all_names,4)
# 训练集
# bg_names=random.sample(bg_all_names,10)

file=open('data/generate_test_data.txt',mode='w')
# image
for fg_name in video_fg_all_names:
   for bg_name in bg_names:
      # fg= fg_name.split('.')[-2]
      # bg= bg_name.split('.')[-2]
      file.write("image"+"+"+fg_name+"+"+bg_name+"\n")

# video
for fg_name in image_fg_all_names:
   for bg_name in bg_names:
      fg = fg_name.split('.')[-2]
      file.write("video" + "+" + fg + "+" + bg_name + ".mp4\n")





