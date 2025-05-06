
new Vue({
    el: '#app',
    data() {
        return {
            city: '',
            hourlyWeather: [],
            futureWeather: [],
            total_time: 0
        };
    },
    methods: {
        async getWeather() {
            if (!this.city) {
                alert("城市名称不能为空");
                this.hourlyWeather = [];
                this.futureWeather = [];
                return;
            }
            // 异步弹出 "请耐心等待"
            setTimeout(() => {
                alert("请耐心等待约30s，点击“确定”以继续");
            }, 0);  // 将弹出提示放在下一个事件循环中，避免阻塞后续代码执行
            try {
                const response = await axios.get(`/api/weather?city=${this.city}`);
                if (response.data.error) {
                    this.hourlyWeather = [];
                    this.futureWeather = [];
                    alert(response.data.error);
                } else {
                    this.hourlyWeather = response.data.hourly_weather;
                    this.futureWeather = response.data.future_weather;
                      // 获取并显示耗时
                    const totalTime = response.data.total_time;  // 获取后端返回的总耗时
                    alert(`查询耗时: ${totalTime} 秒，点击“确定”查看结果`);
                    this.drawHourlyChart();
                    this.drawFutureChart();
                }
            } catch (error) {
                this.hourlyWeather = [];
                this.futureWeather = [];
                alert("请求失败，请稍后再试");
            }
        },

         // 绘制24小时天气图
        drawHourlyChart() {
            var hourlyChart = echarts.init(document.getElementById('hourlyChart'));
            var hourlyData = this.hourlyWeather.map(item => ({
                time: item.time,
                temperature: parseInt(item.temperature)
            }));

            var option = {
                title: {
                    text: '24小时天气',
                },
                xAxis: {
                    type: 'category',
                    data: hourlyData.map(item => item.time)
                },
                yAxis: {
                    type: 'value',
                    name: '温度 (°C)'
                },
                series: [{
                    data: hourlyData.map(item => item.temperature),
                    type: 'line',
                    smooth: true
                }]
            };

            hourlyChart.setOption(option);
        },

        // 绘制未来几天天气图
        drawFutureChart() {
            var futureChart = echarts.init(document.getElementById('futureChart'));
            var futureData = this.futureWeather.map(item => ({
                date: item.date,
                tempRange: item.temperature_range.split('~').map(temp => parseInt(temp))
            }));

            var option = {
                title: {
                    text: '未来几天天气',
                },
                xAxis: {
                    type: 'category',
                    data: futureData.map(item => item.date)
                },
                yAxis: {
                    type: 'value',
                    name: '温度 (°C)'
                },
                series: [{
                    data: futureData.map(item => item.tempRange[0]),
                    type: 'line',
                    smooth: true,
                    name: '最低温度'
                }, {
                    data: futureData.map(item => item.tempRange[1]),
                    type: 'line',
                    smooth: true,
                    name: '最高温度'
                }]
            };
            futureChart.setOption(option);

        }
    }
});
