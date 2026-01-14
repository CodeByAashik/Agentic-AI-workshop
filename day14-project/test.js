fetch("http://localhost:8000/todos").then((response) => response.json()).then((data) => {
  console.log(data);
});