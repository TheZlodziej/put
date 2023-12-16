<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Led matrix</title>
    <style>
        section#container {
            max-height: 500px;
        }
    </style>
</head>
<body>
    <section id="container">
    </section>

    <script>
        (function() {
            function addStyles(el, styles) {
                for(const [nam, val] of Object.entries(styles)) {
                    el.style[nam] = val;
                }
            }

            const makePixel = (i) => {
                const px = document.createElement("input");
                px.type = "color";
                addStyles(px, {
                    all: "unset",
                    cursor: "pointer",
                });

                // input with debouncing
                let timeoutId = null;
                px.addEventListener("input", () => {
                    if(timeoutId) {
                        clearTimeout(timeoutId);
                    }
                    timeoutId = setTimeout(async () => {
                        fetch("./server.php", { method: "POST", body: { num:i, color:px.value } });
                        timeoutId = null;
                    }, 400);
                });
                //

                return px;
            }

            const makeMatrix = (w, h) => {
                const mat = document.createElement("section");
                mat.id = "mat";
                addStyles(mat, {
                    display: "grid",
                    "grid-template-rows": `repeat(${h}, minmax(30px, 1fr))`,
                    "grid-template-columns": `repeat(${w}, minmax(30px, 1fr))`,
                    "row-gap": "10px",
                    "column-gap": "10px",
                    width: "100%",
                    height: "100%",
                    "aspect-ratio":"1/1",
                });
                for(let i=0; i<w*h; i++) {
                    mat.appendChild(makePixel(i));
                }
                return mat;
            }
            
            const matrix = makeMatrix(8, 8);

            const initPixels = async () => {
                return fetch("./server.php")
                    .then(r=>r.json())
                    .then(json => {
                        const px_vals = json["led_matrix"];
                        px_vals.forEach((val, idx) => {
                            matrix.childNodes[idx].value = val;
                     });
	
                })
            }
            
            initPixels();
	    setInterval(initPixels, 3000);
            document.getElementById("container").appendChild(matrix);
        })();
    </script>
</body>
</html>
