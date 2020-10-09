import { readCSV } from './csvReader.js';
import { require } from './modules/require.js';

var myIcon = L.divIcon({className: 'map-label-arrow'});
var mymap = L.map('mapid').setView([52.44901, 13.28204], 17);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar', attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'}).addTo(mymap);    
readCSV("fhi_campus.csv",function(result){
    var fhi_campus = L.polygon(result);
    fhi_campus.addTo(mymap);;
});

readCSV("fhi_campus.csv",function(result){
    var fhi_campus = L.polygon(result);
    var markers = [];
    for(var i=0;i<result.length;i++){
        markers[i] = L.marker(result[i]).addTo(mymap);
        markers[i].bindPopup((i+1).toString());
    }
});
var fs = require('fs');
var sourceFolder = Folder("./plants/");
var files = new Array();
files = sourceFolder.getFiles();
console.log(files)


//var fhi_campus = L.polygon([], smoothFactor = 10.0, noClip = true);
//fhi_campus.addTo(mymap);
//var marker1 = L.marker([52.45006, 13.28170]).addTo(mymap);
//var kuchen1 = L.marker([52.44844, 13.28310]).addTo(mymap);
//kuchen1.bindPopup(fhi_campus.getLatLngs().toString());
//map.fitBounds(fhi_campus.getBounds());  