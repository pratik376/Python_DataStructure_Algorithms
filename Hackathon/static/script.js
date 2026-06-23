const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const calcPanel = document.getElementById("calc-content");

canvas.width = 1500;
canvas.height = 900;

let layers = { input: [], hidden: [], output: [] };
let edges = [];

const positions = { input: 200, hidden: 700, output: 1200 };
const nodeSpacing = 80;

// ---------- ADD NEURON ----------
function addNeuron(type) {
    let neuron = {
        id: type + "_" + Date.now(),
        value: type === "input" ? 1 : 0,
        bias: type === "input" ? 0 : Math.random(),
        blink: false // <-- added for blinking
    };
    layers[type].push(neuron);
    autoConnect();
    draw();
}

// ---------- CONNECT ----------
function autoConnect() {
    edges = [];

    layers.input.forEach(i => {
        layers.hidden.forEach(h => {
            edges.push({ from: i.id, to: h.id, weight: Math.random() });
        });
    });

    layers.hidden.forEach(h => {
        layers.output.forEach(o => {
            edges.push({ from: h.id, to: o.id, weight: Math.random() });
        });
    });
}

// ---------- POSITION ----------
function getPosition(type, index) {
    return { x: positions[type], y: 120 + index * nodeSpacing };
}

// ---------- DRAW ----------
function draw(highlightEdge=null, highlightNode=null, dotPos=null, reverse=false) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    edges.forEach(e => {
        let from = findNode(e.from);
        let to = findNode(e.to);

        let p1 = getPosition(from.type, from.index);
        let p2 = getPosition(to.type, to.index);

        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.strokeStyle = highlightEdge === e ? "#f43f5e" : "#aaa";
        ctx.lineWidth = highlightEdge === e ? 3 : 1;
        ctx.stroke();

        ctx.fillStyle = "white";
        ctx.fillText(e.weight.toFixed(2), (p1.x+p2.x)/2, (p1.y+p2.y)/2);

        if (highlightEdge === e && dotPos !== null) {
            let t = reverse ? 1 - dotPos : dotPos;
            let x = p1.x + (p2.x - p1.x) * t;
            let y = p1.y + (p2.y - p1.y) * t;

            ctx.beginPath();
            ctx.arc(x, y, 6, 0, 2*Math.PI);
            ctx.fillStyle = reverse ? "#f43f5e" : "#22c55e";
            ctx.fill();
        }
    });

    Object.keys(layers).forEach(type => {
        layers[type].forEach((node, i) => {
            let {x,y} = getPosition(type, i);

            ctx.beginPath();
            ctx.arc(x,y,22,0,2*Math.PI);

            // ---------- BLINK EFFECT ----------
            if(node.blink){
                ctx.fillStyle = "#ffff00"; // bright yellow for blink
            } else {
                ctx.fillStyle =
                    type==="input"?"green":
                    type==="hidden"?"blue":"red";
            }

            ctx.fill();

            ctx.fillStyle="white";
            ctx.fillText(node.value.toFixed(2), x-15, y+5);
        });
    });
}

// ---------- FIND ----------
function findNode(id) {
    for (let type in layers) {
        for (let i = 0; i < layers[type].length; i++) {
            if (layers[type][i].id === id) {
                layers[type][i].type = type;
                layers[type][i].index = i;
                return layers[type][i];
            }
        }
    }
}

// ---------- FORWARD ----------
async function animateForward() {

    const section = document.createElement("div");
    section.innerHTML = `<h2>🔵 Forward Pass</h2>`;
    calcPanel.appendChild(section);

    // -------- Hidden Layer --------
    if (layers.hidden.length > 0) {
        section.innerHTML += `<h3>Hidden Layer</h3>`;
    }

    for (let h of layers.hidden) {
        let incoming = edges.filter(e => e.to === h.id);

        let formula = `Neuron ${layers.hidden.indexOf(h)+1}:<br>`;
        formula += `z = b(${h.bias.toFixed(2)}) + `;

        for (let e of incoming) {
            let from = findNode(e.from);

            formula += `(${from.value.toFixed(2)} * ${e.weight.toFixed(2)}) + `;

            // animation along edge
            for (let t = 0; t <= 1; t += 0.1) {
                draw(e, from, t);
                await sleep(30);
            }
        }

        // compute
        h.z = incoming.reduce(
            (sum, e) => sum + findNode(e.from).value * e.weight,
            0
        ) + h.bias;

        h.value = sigmoid(h.z);

        // ---------- BLINK EFFECT ----------
        h.blink = true;
        draw();
        await sleep(200); // blink duration
        h.blink = false;
        draw();

        // finalize formula
        formula = formula.slice(0, -3);
        formula += `<br>activation = sigmoid(${h.z.toFixed(2)}) = ${h.value.toFixed(2)}`;

        section.innerHTML += `<p>${formula}</p>`;
    }

    // -------- Output Layer --------
    if (layers.output.length > 0) {
        section.innerHTML += `<h3>Output Layer</h3>`;
    }

    for (let o of layers.output) {
        let incoming = edges.filter(e => e.to === o.id);

        let formula = `Neuron ${layers.output.indexOf(o)+1}:<br>`;
        formula += `z = b(${o.bias.toFixed(2)}) + `;

        for (let e of incoming) {
            let from = findNode(e.from);

            formula += `(${from.value.toFixed(2)} * ${e.weight.toFixed(2)}) + `;

            for (let t = 0; t <= 1; t += 0.1) {
                draw(e, from, t);
                await sleep(30);
            }
        }

        // compute
        o.z = incoming.reduce(
            (sum, e) => sum + findNode(e.from).value * e.weight,
            0
        ) + o.bias;

        o.value = sigmoid(o.z);

        // ---------- BLINK EFFECT ----------
        o.blink = true;
        draw();
        await sleep(200); // blink duration
        o.blink = false;
        draw();

        // finalize formula
        formula = formula.slice(0, -3);
        formula += `<br>activation = sigmoid(${o.z.toFixed(2)}) = ${o.value.toFixed(2)}`;

        section.innerHTML += `<p>${formula}</p>`;
    }

    // auto-scroll
    calcPanel.scrollTo({
        top: calcPanel.scrollHeight,
        behavior: "smooth"
    });
}

// ---------- BACKPROP ----------
async function startBackprop() {

    let numOutputs = layers.output.length;
    if (numOutputs === 0) return alert("Add output neuron!");

    let input = prompt(
        numOutputs === 1
        ? "Enter target value:"
        : `Enter ${numOutputs} values (comma separated)`
    );

    if (!input) return;

    let targets = numOutputs === 1
        ? [parseFloat(input)]
        : input.split(",").map(x => parseFloat(x.trim()));

    if (targets.length !== numOutputs || targets.some(isNaN)) {
        alert("Invalid target input!");
        return;
    }

    const section = document.createElement("div");
    section.innerHTML = `<h2>🔴 Backpropagation</h2>`;
    calcPanel.appendChild(section);

    const lr = 0.1;

    // ================= LOSS =================
    let loss = 0;

    layers.output.forEach((o,i)=>{
        let l = Math.pow(targets[i] - o.value, 2);
        loss += l;

        section.innerHTML += `<p>Loss${i+1}: (${targets[i].toFixed(2)} - ${o.value.toFixed(2)})² = ${l.toFixed(4)}</p>`;
    });

    loss /= layers.output.length;
    section.innerHTML += `<b>Total Loss: ${loss.toFixed(4)}</b>`;

    // ================= OUTPUT GRAD =================
    for (let i = 0; i < layers.output.length; i++) {
        let o = layers.output[i];
        let dLoss = -2*(targets[i] - o.value);
        let dOut = o.value * (1 - o.value);
        o.grad = dLoss * dOut;

        // ---------- BACKWARD EDGE ANIMATION ----------
        let incoming = edges.filter(e => e.to === o.id);
        for (let e of incoming) {
            let from = findNode(e.from);
            for (let t = 0; t <= 1; t += 0.1) {
                draw(e, from, t, true); // reverse = true
                await sleep(20);
            }
        }

        // ---------- BLINK EFFECT ----------
        o.blink = true;
        draw();
        await sleep(200);
        o.blink = false;
        draw();
    }

    // ================= HIDDEN GRAD =================
    for (let i = layers.hidden.length - 1; i >= 0; i--) {
        let h = layers.hidden[i];

        let outgoing = edges.filter(e => e.from === h.id);
        let sum = 0;

        for (let e of outgoing) {
            let outNode = layers.output.find(o => o.id === e.to);
            sum += e.weight * outNode.grad;

            // ---------- BACKWARD EDGE ANIMATION ----------
            for (let t = 0; t <= 1; t += 0.1) {
                draw(e, h, t, true); // reverse = true
                await sleep(20);
            }
        }

        let dOut = h.value * (1 - h.value);
        h.grad = sum * dOut;

        // ---------- BLINK EFFECT ----------
        h.blink = true;
        draw();
        await sleep(200);
        h.blink = false;
        draw();
    }

    // ================= UPDATE WEIGHTS =================
    edges.forEach(e => {
        let from = findNode(e.from);
        let toNode =
            layers.hidden.find(n => n.id === e.to) ||
            layers.output.find(n => n.id === e.to);
        let grad = toNode.grad || 0;
        e.weight -= lr * grad * from.value;
    });

    // ================= UPDATE BIASES =================
    [...layers.hidden, ...layers.output].forEach(n=>{
        n.bias -= lr * (n.grad || 0);
    });

    draw(); // final canvas update
}
// ---------- UTILS ----------
function sigmoid(x){ return 1/(1+Math.exp(-x)); }
function sleep(ms){ return new Promise(r=>setTimeout(r,ms)); }

function clearAll(){
    layers = { input: [], hidden: [], output: [] };
    edges = [];
    calcPanel.innerHTML="";
    draw();
}

// ---------- EDIT INPUT ----------
canvas.addEventListener("click", function(evt){
    let x=evt.offsetX,y=evt.offsetY;

    layers.input.forEach(n=>{
        let p=getPosition("input",layers.input.indexOf(n));
        if(Math.hypot(x-p.x,y-p.y)<22){
            let v=prompt("value:",n.value);
            if(v!==null)n.value=parseFloat(v);
            draw();
        }
    });
});

draw();