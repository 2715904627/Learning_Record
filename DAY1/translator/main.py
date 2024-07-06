import random

def main():
    while True:
        num = random.randint(0, 15)
        bin_num = bin(num)[2:].zfill(4)
        hex_num = hex(num)[2:].zfill(1).upper()

        # print("2进制数: ", bin_num)
        # user_hex = input("输入此2进制数对应的16进制数 (或输入'q'退出): ")
        # if user_hex.lower() == 'q':
        #     break
        # elif user_hex.upper() != hex_num:
        #     print("错误，正确的16进制数是: ", hex_num)
        # else:
        #     print("正确")

        print("16进制数: ", hex_num)
        user_bin = input("输入此16进制数对应的2进制数 (或输入'q'退出): ")
        if user_bin.lower() == 'q':
            break
        elif user_bin != bin_num:
            print("错误，正确的2进制数是: ", bin_num)
        else:
            print("正确")

if __name__ == "__main__":
    main()
