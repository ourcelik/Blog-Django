async function fetchPosts(url) {
  let titles = [];
  const response = await fetch(`${url}`);
  const data = await response.json();
  data.forEach(Post => {
    titles.push(Post.fields)
    console.log(Post.fields)
  })
  return titles;
}


async function Changearea(url) {
  const data = await fetchPosts(url);
  var titles = document.querySelectorAll(".c-title");
  var summaries = document.querySelectorAll(".c-contentarea")
  var images = document.querySelectorAll(".c-context-img")

  for (let i = 0; i < titles.length; i++) {
    titles[i].innerHTML = data[i].title;
    summaries[i].innerHTML = data[i].summary;
    images[i].src = `./media/${data[i].image}`;
  }
}
function getCsharpPosts() {
  url = './json/csharp'
  setTimeout(Changearea, 0, url);
}

function getJavascriptPosts() {
  url = './json/javascript'
  setTimeout(Changearea, 0, url);
}
function getCssPosts() {
  url = './json/css'
  setTimeout(Changearea, 0, url);
}
function getPythonPosts() {
  url = './json/python'
  setTimeout(Changearea, 0, url);
}
function getHtmlPosts() {
  url = './json/html'
  setTimeout(Changearea, 0, url);
}