let dados = [];
let grafico = new Chart(document.getElementById("grafico"), {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Temperatura °C",
        data: dados,
        borderColor: "#00ffc3",
        fill: false,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: { legend: { display: false } },
    scales: { y: { display: false }, x: { display: false } },
  },
});

async function atualizar() {
  try {
    let res = await fetch("/temperatura");
    let json = await res.json();

    let c = json.temp;
    let f = c * 1.8 + 32;
    let k = c + 273.15;

    document.getElementById("celsius").innerText = c.toFixed(2) + " °C";
    document.getElementById("fahrenheit").innerText = f.toFixed(2) + " °F";
    document.getElementById("kelvin").innerText = k.toFixed(2) + " K";

    dados.push(c);
    grafico.data.labels.push("");
    if (dados.length > 20) {
      dados.shift();
      grafico.data.labels.shift();
    }
    grafico.update();
  } catch (e) {
    console.error("Erro ao atualizar:", e);
  }
}

setInterval(atualizar, 1000);
