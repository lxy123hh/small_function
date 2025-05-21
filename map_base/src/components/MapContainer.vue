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
  const map = new AMap.Map('map', {
    center: [116.397428, 39.90923],
    zoom: 12,
  });

  new AMap.Marker({
    position: [116.397428, 39.90923],
    map: map,
    title: '天安门',
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