const w = parseInt(readline());
const h = parseInt(readline());
const text = readline();

let alphabet = [];

for (let i=0; i<h; i++) {
    alphabet.push(readline());
}

function get_alphabetical_idx(letter)
{
    letter = letter.toUpperCase();
    if(letter.charCodeAt(0) >= 'A'.charCodeAt(0) && letter.charCodeAt(0) <= 'Z'.charCodeAt(0))
        return (letter[0].charCodeAt(0) - 'A'.charCodeAt(0))
    return 26; //?
}

let opt=[];

for(let i=0; i<h; i++)
{
    let row=[];
    for(let letter of text)
    {
        row.push(alphabet[i].substr(get_alphabetical_idx(letter)*w, w));
    }
    opt.push(row.join(""));
}

for(let row of opt)
{
    print(row);
}
