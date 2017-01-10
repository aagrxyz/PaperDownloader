var foo =  require("./get_papers");
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter your IITD Entry Number\n', (answer) => 
{
	foo.get_papers(answer);
	console.log("Get your zip file in the output directory \n")
    rl.close();
});


