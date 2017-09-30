
# coding:utf-8

def exchange_mask(mask):
    """
    转换子网掩码格式
    """

    # 计算二进制字符串中 '1' 的个数
    count_bit = lambda bin_str: len([i for i in bin_str if i=='1'])

    # 分割字符串格式的子网掩码为四段列表
    mask_splited = mask.split('.')

    # 转换各段子网掩码为二进制, 计算十进制
    mask_count = [count_bit(bin(int(i))) for i in mask_splited]

    return sum(mask_count)
    #www.iplaypy.com

if __name__ == '__main__':
    print exchange_mask('255.255.0.0')