from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image       # 注意：python3需要安装Pillow模块！！！
import pytesser3

class ForgetPassword():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = url = 'http://passport.ziroom.com/index.php?r=user%2Fforget-password'
        self.number = '13986037701'
        self.login_url()

    def login_url(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)
        self.input_phonenumber()

    def input_phonenumber(self):
        phone_input = self.driver.find_element_by_id('J-m-user')
        text = self.driver.find_element_by_xpath('//*[@id="J-m-user"]').text
        print(text)
        if text is self.number:
            self.input_image()

        else:
            print('正在输入手机号')
            phone_input.clear()
            phone_input.send_keys(self.number)
            self.input_image()

    def input_image(self):
        # 保存网页截图
        self.driver.save_screenshot('F:/JingBaoBao/ShuaPiao of JJ/NumberImage.png')

        # 定位外网上验证码图片位置、大小，并计算出坐标
        image = self.driver.find_element_by_xpath('//*[@id="J-m-img"]')
        location = image.location
        size = image.size
        zuobiao = (location['x'], int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

        # 打开之前的网页截图
        screenshot_big = Image.open('F:/JingBaoBao/ShuaPiao of JJ/NumberImage.png')
        # 使用Image的crop函数，根据坐标切割我们需要的区域
        screenshot_small = screenshot_big.crop(zuobiao)
        # 保存切割后的图片
        screenshot_small.save('F:/JingBaoBao/ShuaPiao of JJ/SmallImage.png')


        # 通过算法来进行图像字符识别处理
        transer_color = Image.open('F:/JingBaoBao/ShuaPiao of JJ/SmallImage.png')

        gray = transer_color.convert('L')                             # 将RGB彩图转换为灰度图
        gray.save('F:/JingBaoBao/ShuaPiao of JJ/Gray1.png')
        gray.save('F:/JingBaoBao/ShuaPiao of JJ/Gray2.png')
        transer_gray2 = Image.open('F:/JingBaoBao/ShuaPiao of JJ/Gray2.png')

        bin = gray.convert('1')                                # 将灰度图转换为二值化图
        bin.save('F:/JingBaoBao/ShuaPiao of JJ/Bin.png')       # 利用convert函数将灰度图转换为二值图时，是采用固定的阈值127来实现的，即灰度高于127的像素值为1，而灰度低于127的像素值为0。
        transer_bin = Image.open('F:/JingBaoBao/ShuaPiao of JJ/Bin.png')


        # 处理每一个像素点颜色
        width = transer_color.size[0]  # 长度
        height = transer_color.size[1]  # 宽度
        xiabiao = []
        for i in range(0, width):  # 遍历所有长度的点
            for j in range(0, height):  # 遍历所有宽度的点
                data = (transer_color.getpixel((i, j)))  # 获取该像素点的RGBA值
                rgb = [data[0],data[1],data[2]]
                print('之前：',rgb)        # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
                #print (data[0])    # 打印RGBA的r值
                for x in rgb:
                    if x > 199:  # RGBA值的判断
                        a = rgb.index(x)
                        print(a)
                        x = x - 200
                        xiabiao.append((a,x))
                        print(xiabiao)
                    else :
                        pass
                if xiabiao is None:
                    pass
                elif len(xiabiao) ==1:
                    if xiabiao[0][0] == 0:
                        transer_color.putpixel((i, j), (xiabiao[0][1],rgb[1],rgb[2],255))
                        transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                        transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片

                    elif xiabiao[0][0] == 1:
                        transer_color.putpixel((i, j), (rgb[0],xiabiao[0][1], rgb[2], 255))
                        transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                        transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片
                    elif xiabiao[0][0] == 2:
                        transer_color.putpixel((i, j), (rgb[0],rgb[1], xiabiao[0][1], 255))
                        transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                        transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片
                elif len(xiabiao) == 2:
                    if xiabiao[0][0] ==0 and xiabiao[1][0] ==1:
                        transer_color.putpixel((i, j), (xiabiao[0][1], xiabiao[1][1], rgb[2], 255))
                        transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                        transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片
                    elif xiabiao[0][0] == 1 and xiabiao[1][0] == 2:
                        transer_color.putpixel((i, j), (rgb[0], xiabiao[1][1], xiabiao[2][1], 255))
                        transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                        transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片
                    elif xiabiao[0][0] == 0 and xiabiao[1][0] == 2:
                        transer_color.putpixel((i, j), (xiabiao[0][1], rgb[1], xiabiao[2][1], 255))
                        transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                        transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片
                elif len(xiabiao) == 3:
                    transer_color.putpixel((i, j), (xiabiao[0][1], xiabiao[1][1], xiabiao[2][1], 255))
                    transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                    transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片


                transer_color = transer_color.convert("RGB")  # 把图片强制转成RGB
                transer_color.save('F:/JingBaoBao/ShuaPiao of JJ/Color2.png')  # 保存修改像素点后的图片


    '''
        # 通过pytesser3模块进行图像字符识别
        transer  = Image.open('F:/JingBaoBao/ShuaPiao of JJ/SmallImage.png')
        text = pytesser3.image_to_string(transer)
        print(text)
        '''

    def input_message(self):
        pass

ForgetPassword()
