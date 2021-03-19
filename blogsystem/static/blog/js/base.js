
var bool = false;
var newsIndex = 0;
NotifyArea(newsIndex);
setInterval(() => {
  newsIndex++;
  NotifyArea(newsIndex % 7);
}, 2000);
function toggle_oc() {
  setTimeout(() => {
    let _sidebar = document.getElementById('sidebar');
    let main = document.getElementById('main');
    bool = !bool;
    if (bool) {
      _sidebar.style.left = "-35vh";
      main.style.left = '5%';
      main.style.width = '90%';
    }
    else {
      _sidebar.style.left = "0";
      main.style.left = '25%';
      main.style.width = '70%';
    }
  }, 0);

}
// function BringText(event)
// {
//   let elem = event.target.childNodes;
//   let summary = elem[1];
//   summary.style.fontSize = "18px";
//   summary.style.display = "block";
//   summary.style.color = "white";


// }

function HideText(event) {
  let elem = event.target.childNodes;
  let summary = elem[1];
  summary.style.fontSize = "17px";

}

function NotifyArea(index) {
  const news = {
    "0": "Populer haber 1",
    "1": "Populer haber 2",
    "2": "Populer haber 3",
    "3": "Populer haber 4",
    "4": "Populer haber 5",
    "5": "Populer haber 6",
    "6": "Populer haber 7",
    "7": "Populer haber 8",
  }
  let text = document.getElementById('NotifyText');
  let link = text.parentElement;
  link.href = `#${index + 1}`;
  text.innerHTML = news[index];

}