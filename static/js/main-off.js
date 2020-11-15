var title = "Daniel Melchor";
var msg = ["Hi, I'm Dani! I am currently a Computer Science major at Boston University (class of 2024). I have been coding since I was 8 and it has been my passion ever since.","This is my portfolio, welcome! :)"];

var index = 0;

var doing = 0;

function checkIfDone(){
  if (app.title == title && doing == 0) {
    clearInterval(timer);
    setTimeout(function() { app.nottyping = true; }, 200);
    doing = 1;
    app.descrGen();
  }
}

function doSetTimeout(i,j) {
  setTimeout(function(){ changeij(i,j); },200+30*i+j*(msg[0].length*30));
}

function changeij(i,j) {
  app.nottyping2 = [true,true];
  app.nottyping2[j] = false;
  Vue.set(app.msg, j, app.msg[j] + msg[j][i]);

  if(app.msg[j] == msg[j]) {
    if(j == 1) {
      app.donetyping = true;
    } else {
      app.nottyping2[j] = true;
    }
  }
}

var app = new Vue({
  el: '#app',
  delimiters: ["[[","]]"],
  data: {
    title: title,
    msg: ['','','',''],
    nottyping : true,
    nottyping2 : [true,true,true,true],
    donetyping : false
  },
  methods: {
    titleGen: function (){
      index += 1;
      this.nottyping = false;
      this.title = title.slice(0,index);
      checkIfDone();
    },
    descrGen: function (){
      for(j=0;j<2;j++) {
        for(i=0;i<msg[j].length;i++) {
          doSetTimeout(i,j);
        }
      }
    }
  }
})

timer = setInterval(app.titleGen,120);
