// ==UserScript==
// @name         0hh1 completer?
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://0hh1.com/
// @grant        none
// ==/UserScript==

var board = [['2', '2', '1', '1', '2', '1', '2', '1', '2', '1', '1', '2'],
             ['1', '1', '2', '2', '1', '2', '2', '1', '1', '2', '1', '2'],
             ['1', '2', '2', '1', '2', '1', '1', '2', '1', '2', '2', '1'],
             ['2', '1', '1', '2', '2', '1', '2', '1', '2', '1', '2', '1'],
             ['2', '1', '2', '1', '1', '2', '1', '2', '2', '1', '1', '2'],
             ['1', '2', '2', '1', '2', '1', '1', '2', '1', '2', '1', '2'],
             ['1', '2', '1', '2', '1', '2', '2', '1', '1', '2', '2', '1'],
             ['2', '1', '1', '2', '1', '2', '2', '1', '2', '1', '2', '1'],
             ['2', '1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '2'],
             ['1', '2', '1', '2', '1', '2', '1', '2', '1', '2', '1', '2'],
             ['2', '1', '2', '1', '2', '1', '2', '1', '2', '1', '2', '1'],
             ['1', '2', '1', '2', '1', '2', '1', '2', '2', '1', '2', '1']];
myFunction = function(){
    for(i=0;i<board.length;i++){
        for(j=0;j<board[0].length;j++){
            var index = j*(board.length)+i;
            tiles[index].set(board[j][i]);
        }
    }
};

add = function(){
    console.log("HI");
    var node = document.createElement("BUTTON");
    var text = document.createTextNode("Start the script AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH");
    node.appendChild(text);
    $("#boardsize").append(node);
};
p = $('[data-action="gift"]')[0];
console.log(p);
p.addEventListener('click', add);   //I've done this three ways
p.onClick=add;                      //Why don't any of them work
p.setAttribute('onclick', 'add()'); //Let's add something new
$('[data-action="gift"]')[0].addEventListener('click', add);