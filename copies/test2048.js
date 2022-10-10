class test2048 {
    validateTestCase(testBoard, direction, boardResult) {
      var objGameTest = new game2048;
      objGameTest.gameBoard = testBoard;
      switch(direction){
        case 'Left': objGameTest.boardDirectionMoves('Left'); break;
        case 'Down': objGameTest.boardDirectionMoves('Down'); break;
        case 'Right': objGameTest.boardDirectionMoves('Right'); break;
        case 'Up': objGameTest.boardDirectionMoves('Up'); break;
      }
      console.assert((','+ objGameTest.gameBoard.join()+',') === (','+boardResult.join()+',')); 
    }

    testCases() {
      this.validateTestCase([[0,0,0,2], [0,0,8,0], [0,4,0,0], [2,0,0,0]], 'Down', [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [2,4,8,2] ] );
      this.validateTestCase([[0,0,2,2], [0,2,0,0], [2,0,0,2], [2,2,2,2]], 'Down', [ [0,0,0,0], [0,0,0,0], [0,0,0,2], [4,4,4,4] ] );
      this.validateTestCase([[0,0,2,2], [0,2,0,0], [2,0,0,2], [2,2,2,2]], 'Right', [ [0,0,0,4], [0,0,0,2], [0,0,0,4], [0,0,4,4] ] );
      this.validateTestCase([[0,0,2,2], [0,2,0,0], [2,0,0,2], [2,2,2,2]], 'Up', [ [4,4,4,4], [0,0,0,2], [0,0,0,0], [0,0,0,0] ] );
      this.validateTestCase([[0,0,2,2], [0,2,0,0], [2,0,0,2], [2,2,2,2]], 'Left', [ [4,0,0,0], [2,0,0,0], [4,0,0,0], [4,4,0,0] ] );
      this.validateTestCase([[2048,8,4,2], [0,2,4,0], [0,2,8,2], [2048,8,0,4]], 'Down', [ [0,0,0,0], [0,8,0,0], [0,4,8,4], [4096,8,8,4] ] );
      this.validateTestCase([[2,2,2,2], [2,2,2,2], [2,2,2,2], [2,2,2,2]], 'Down', [ [0,0,0,0], [0,0,0,0], [4,4,4,4], [4,4,4,4] ] );
      this.validateTestCase([[0,4,0,2], [2,2,2,0], [2,8,4,0], [32,4,32,8]], 'Right', [ [0,0,4,2], [0,0,2,4], [0,2,8,4], [32,4,32,8] ] );
      this.validateTestCase([[8,0,0,4], [0,0,0,2], [16,0,4,0], [32,4,16,8]], 'Left', [ [8,4,0,0], [2,0,0,0], [16,4,0,0], [32,4,16,8] ] );
      this.validateTestCase([[8,0,0,4], [2,0,0,0], [16,0,4,0], [32,4,16,8]], 'Right', [ [0,0,8,4], [0,0,0,2], [0,0,16,4], [32,4,16,8] ] );
    }
  } // class test2048 ends


  setInterval(function() {
    /*if (Math.floor((Math.random()*2)) == 1) strCurrentOperation="+";
    else strCurrentOperation = "x";*/
    $("#lblCurrentOperation").css("rotateOperator");
  }, 1000);