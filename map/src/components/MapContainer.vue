<template>
    <div id="map"></div>
  </template>
  
  <script>
  import AMapLoader from '@amap/amap-jsapi-loader';
  

  export default {
    name: 'MapContainer',
    mounted() {
      AMapLoader.load({
        key: 'cd3a1dc38f383bbee332dcf3ee972e8a', 
        version: '2.0',
        plugins: [],
      })
        .then((AMap) => {
          new AMap.Map('map', {
            //center: [116.397428, 39.90923], // 初始中心点
            center: [119.5143, 32.1993],
            zoom: 13, // 初始缩放级别
          });
          new Amap.Marker({
            position: [119.5143, 32.1993], // 标记点位置
            map: map, // 添加到地图上
            title: 'Hello World', // 标记点标题
          });
        })
        .catch((e) => {
          console.error(e);
        });
    },
  };
  </script>
  
  <style scoped>
  #map {
    width: 100%;
    height: 500px;
  }

  </style>