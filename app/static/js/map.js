function set_url(url) {
    return function(e){
        window.location.href = url;
    }
}

function loadJson(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

var jsonData = loadJson('#jsonData');


ymaps.ready(init);
        function init(){
            var myMap = new ymaps.Map("map", {
                center: [jsonData[0]['long'], jsonData[0]['lat']],
                zoom: 13
            });


            for (point of jsonData){
                // Размещение геообъекта на карте.
                var geoObj = new ymaps.GeoObject({
                // Описание геометрии.
                        geometry: {
                            type: "Point",
                            coordinates: [point['long'], point['lat']]
                        },
                        // Свойства.
                        properties: {
                            // Контент метки.
                            iconContent: point['price'],
                            hintContent: point['url'],
                            url: point['url'],
                        }
                    }, {
                        // Опции.
                        // Иконка метки будет растягиваться под размер ее содержимого.
                        preset: 'islands#greenStretchyIcon',
                    });
                    var url = geoObj.properties._data['url']
                    geoObj.events.add('click', set_url(url))
                    myMap.geoObjects.add(geoObj)
            }

        }