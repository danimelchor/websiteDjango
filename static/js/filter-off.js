tags = ["HTML","CSS","PHP","Jquery","Python","Django","VueJS","SASS"];

window.onload = function () {
  var filter = new Vue({
    el: '#filterdiv',
    delimiters: ["[[","]]"],
    data: {
      filters: tags
    }
  });
}
