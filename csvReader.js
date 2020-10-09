export function readCSV(pFilename, callback){
    return $.get(pFilename, function(fileContent){
        var lines = fileContent.split("\n");
        var poly = [];
        for(var i=0;i<lines.length;i++){
            var row = lines[i];
            poly[i] = lines[i].split(", ");
        }
        //poly=poly.slice(0,-1);
        callback(poly);
    });
}