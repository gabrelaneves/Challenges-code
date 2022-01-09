

var arr = (["ahffaksfajeeubsne", ("jefaa")]);

function StringC(strArr) {
    var n = strArr[0].split("");
    var k = strArr[1].split("");
    var [s, x, len_k] = [0, 0, k.length];


    while (x <= n.length) {
        for (x = len_k; x < n.length; x++) {

            var a = n.slice(s, x);

            var uni_k = [...new Set(k)];
            var uni_a = [...new Set(a)];


            let checker = (arr, target) => target.every(v => arr.includes(v));

            var found = checker(uni_a, uni_k);
            if (found) {
                var b = n.slice(s, x);
                var p = strArr[1].split("");


                // vincula o recurso
                for (var t of k) {

                    var l_b_1 = b.indexOf(t);
                    console.log(l_b_1);

                    b.splice(b.indexOf(t), 1);


                    if (l_b_1 != -1) {
                        p.splice(p.indexOf(t), 1);
                    }

                    if (p.length == 0) {
                        return a;

                    }
                }
            }
            s = s + 1;

        }


        // more statements
        s = 0;
        len_k = len_k + 1;
    }
}

console.log(StringC(arr));