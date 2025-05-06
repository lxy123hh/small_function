import re

import requests
from flask import Flask, render_template, jsonify, request
import time
from pypinyin import pinyin, Style
app = Flask(__name__)


# 将中文城市名转换为拼音
def convert_to_pinyin(city_name):
    pinyin_list = pinyin(city_name, style=Style.NORMAL)  # 转换为拼音

    # 拼接拼音，忽略声调
    return ''.join([item[0] for item in pinyin_list])

# 获取24小时内天气和未来几天天气
def get_weather_data(city):
    start_time = time.time()

    city = convert_to_pinyin(city)

    # 构建请求的 URL
    url = f'https://m.tianqi.com/{city}/'


    # 添加请求头，模拟浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

    # 发送请求
    response = requests.get(url, headers=headers)

    # 检查响应状态
    if response.status_code != 200:
        print(f"Failed to fetch data for {city}, Status code: {response.status_code}")
        return {'hourly_weather': [], 'future_weather': []}

    # 获取网页的文本内容
    html_content = response.text

    # 解析 24 小时天气数据
    hourly_weather = []
    hourly_pattern = re.compile(r'<li>.*?<p>(\d{1,2}时)</p>.*?<span>(.*?)</span>.*?</li>', re.S)
    hourly_data = re.findall(hourly_pattern, html_content)
    for item in hourly_data:
        current_time = item[0]  # 时间
        temperature = item[1]  # 温度
        hourly_weather.append({'time': current_time, 'temperature': temperature})

    # 解析未来几天的天气数据
    future_weather = []
    future_pattern = re.compile(
        r'<a href=".*?">.*?<dt>(.*?)</dt>.*?<dd class="txt">(.*?)</dd>.*?<dd class="txt2">(.*?)</dd>.*?<dd class="txt">(.*?)</dd>.*?</a>',
        re.S)
    future_data = re.findall(future_pattern, html_content)

    # 忽略第一个无关数据（天气预报）
    for item in future_data[1:]:
        day = item[0]  # 周几
        date = item[1]  # 日期
        condition = item[2]  # 天气状况
        temp_range = item[3]  # 温度范围

        # 处理温度范围中的 <b> 标签
        temp_range = re.sub(r'<b.*?>|</b>', '', temp_range)  # 去掉 <b> 标签内容

        future_weather.append({'day': day, 'date': date, 'condition': condition, 'temperature_range': temp_range})

    final_time = time.time()

    total_time = final_time - start_time

    # 打印抓取到的数据，便于调试
    print("Hourly Weather:", hourly_weather)
    print("Future Weather:", future_weather)

    return {
        'hourly_weather': hourly_weather,
        'future_weather': future_weather,
        'total_time': round(total_time, 2),
    }


@app.route('/')
def index():
    return render_template('weather_query.html')
@app.route('/weather_query')
def weather_query():
    return render_template('weather_query.html')

@app.route('/chinese_map')
def chinese_map():
    return render_template('chinese_map.html')
@app.route('/api/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if city:
        data = get_weather_data(city)
        return jsonify(data)
    else:
        return jsonify({"error": "城市名称不能为空"})











if __name__ == "__main__":
    app.run(debug=True)
