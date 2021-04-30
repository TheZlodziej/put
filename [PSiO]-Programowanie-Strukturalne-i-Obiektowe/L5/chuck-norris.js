let msg = readline()
.split("")
.map(x=>x.charCodeAt(0).toString(2))
.map(x=>"0".repeat(7-x.length)+x)
.join("");

let opt=[];

msg = msg.replace(/10/g, "1,0").replace(/01/g, "0,1").split(",");

for(let m of msg)
{
    opt.push(m[0]=="0"?"00":"0");
    opt.push("0".repeat(m.length));
}

print(opt.join(" "));