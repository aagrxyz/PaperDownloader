var courses = [];
var table = document.querySelectorAll("table")[5];
var rows = table.querySelectorAll("tr");

for(var i=1;i<rows.length;i++)
{
	var cols = rows[i].children;
	var dic = {};
	dic.code = cols[2].textContent;
	dic.name = cols[3].textContent;
	dic.credit = cols[4].textContent;
	dic.structure = cols[5].textContent;
	courses.push(dic);
}
console.log(JSON.stringify(courses))

var keys = [];
for (var key in courses) {
  if (courses.hasOwnProperty(key)) {
    keys.push(key);
  }
}