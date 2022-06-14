from H_m3u8DL import m3u8download


def get_color_string(string, fore_color=None, background_color=None):
    """ 得到带有颜色及格式的字符串

    :param string: 需要输出的字符串
    :param fore_color: 字体颜色, 默认无效果
    :param background_color: 背景色, 默认无效果
    :param show_type: 显示方式, 默认无效果
    :return: 带有颜色及格式的字符串
    """
    # 如果全是默认值
    if fore_color is None \
            and background_color is None:
        return string

    # 具有非默认值的情况，也就是有的字符串具有属性
    str = "\033["
    # 增加文字颜色
    if fore_color is not None:
        str = str + ";" + fore_color

    # 增加背景色
    if background_color is not None:
        str = str + ";" + background_color

    # 拼接字符串
    str = str + "m" + string + "\033[0m"

    return str