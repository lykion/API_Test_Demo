# -*- coding:utf-8 -*-
import requests
import json
import config as conf
from common.log import logger


def test_api(method, url, data, headers, is_header):
    """
    自定义的接口测试方法
    :param method: 请求方法
    :param url: 接口地址
    :param data: 请求参数
    :param headers: headers
    :param is_header: 是否有header
    :return: result -- 接口返回的结果
    """
    """
    1、判断接口请求方式、选择对应的请求
    2、判断是否有header，选择对应请求
    """
    try:
        if method == 'POST' or method == 'post':    # post请求
            if is_header == 'YES' or is_header == 'yes':    # 有header
                res = requests.post(url, data, headers=headers)
            else:       # 无header
                res = requests.post(url, json.loads(data))
            result = res.json()
        else:       # get请求
            res = requests.get(url, data)
            result = res.json()
        return result
    except Exception as e:
        logger().error('请求时失败：{}'.format(e))


def get_response_content(method, url, data, headers, is_header):
    """
    自定义检查接口的返回结果
    :param method: 请求方法
    :param url: 接口地址
    :param data: 请求参数
    :param headers: headers
    :param is_header: 是否有header
    :return: content -- 自定义检查的返回结果
    """
    content = []
    try:
        if method == 'POST' or method == 'post':
            if is_header == 'YES' or is_header == 'yes':
                res = requests.post(url, data, headers=headers)
            else:
                res = requests.post(url, json.loads(data))
            code = res.json().get('code')   # 获取code值
            msg = res.json().get('msg')     # 获取msg值
            result = res.json().get('result')   # 获取result值
            content.append(code)
            content.append(msg)
            content.append(result)
        else:
            res = requests.get(url, data)
            code = res.json().get('code')
            msg = res.json().get('msg')
            result = res.json().get('result')
            content.append(code)
            content.append(msg)
            content.append(result)
        return content
    except Exception as e:
        logger().error('请求失败：{}'.format(e))


"""测试类"""
if __name__ == '__main__':
    url = conf.url
    method = conf.method
    data = conf.data
    logger().info(type(data))
    headers = conf.headers
    is_header = conf.is_header
    res = test_api(method, url, json.dumps(data), headers, is_header)
    # content = get_response_content(method, url, json.dumps(data), headers, is_header)
    logger().info(res)
    logger().info(res.get('msg'))
    # logger().info(content)

