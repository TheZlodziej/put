let lon = readline().replace(",", ".");
let lat = readline().replace(",", ".");
let n = parseInt(readline());

let defibs = [];
for (let i = 0; i < n; i++) {
    let defib = readline().split(";");

    let name = defib[1];
    let d_lon = defib[4].replace(",", ".");
    let d_lat = defib[5].replace(",", ".");
    let x = (d_lon-lon)*Math.cos(parseFloat(lat+d_lat)/2)
    let y = d_lat - lat;
    let dist = Math.sqrt(x*x+y*y) * 6371;
    defibs.push({
        name:name,
        dist:dist
    });
}

let min =defibs[0];

for(let defib of defibs)
{
    if(defib.dist<min.dist)
    {
        min=defib;
    }
}

print(min.name);


