function sendPost() {
  const data = JSON.stringify({
    nev: document.getElementById("nev").value,
    husi: document.getElementById("husi").value,
    suly: document.getElementById("suly").value,
    ar: document.getElementById("ar").value,
    daarabszam: document.getElementById("daarabszam").value,
  });

  navigator.sendBeacon("http://127.0.0.1:5000/savedetails/", data);
  console.log(data);
}
