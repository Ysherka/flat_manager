ymaps.ready(init);
        function init(){
            var myMap = new ymaps.Map("map", {
                center: [54.073682, 44.937971],
                zoom: 17
            });

            myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
            geometry: {
                type: "Point",
                coordinates: [54.073682, 44.937971]
            },
            // Свойства.
            properties: {
                // Контент метки.
                iconContent: '5000',
                hintContent: 'Цена'
            }
        }, {
            // Опции.
            // Иконка метки будет растягиваться под размер ее содержимого.
            preset: 'islands#greenStretchyIcon',
        });

            // Размещение геообъекта на карте.
            myMap.geoObjects.add(myGeoObject);
        }