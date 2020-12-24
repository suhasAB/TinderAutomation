var i = 1;                  //  set your counter to 1

function myLoop() {         //  create a loop function
  setTimeout(function() {   //  call a 0.7 s setTimeout when the loop is called
    console.log('liked it');
    document.getElementsByClassName("Pos(r) Z(1)")[4].click();   //  this code will click on like button
    i++;                    //  increment the counter
    if (i < 100) {           //  if the counter < 100, call the loop function-> the # of time you want to press like
      myLoop();             //  ..  again which will trigger another
    }                       //  ..  setTimeout()
  }, 700)
}

myLoop();
