var board1 = null;
var game = new Chess();
console.log(game);
var $status = $('#status')
var $fen = $('#fen')
var $pgn = $('#pgn')

function onDragStart (source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    if (game.isGameOver()) return false
  
    // only pick up pieces for the side to move
    if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
        (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
      return false
    }
}

function onDrop (source, target) {
    // see if the move is legal
    var move = game.move({
      from: source,
      to: target,
      promotion: 'q' // NOTE: always promote to a queen for example simplicity
    })
  
    // illegal move
    if (move === null) return 'snapback'
  
    updateStatus()
}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd () {
    board1.position(game.fen())
}

function updateStatus () {
    var status = ''
  
    var moveColor = 'White'
    if (game.turn() === 'b') {
      moveColor = 'Black'
    }
  
    // checkmate?
    if (game.isCheckmate()) {
      status = 'Game over, ' + moveColor + ' is in checkmate.'
    }
  
    // draw?
    else if (game.isDraw()) {
      status = 'Game over, drawn position'
    }
  
    // game still on
    else {
      status = moveColor + ' to move'
  
      // check?
      if (game.isCheck()) {
        status += ', ' + moveColor + ' is in check'
      }
    }
  
    $status.html(status)
    $fen.html(game.fen())
    $pgn.html(game.pgn())
}

function socketConnect() {
    let url = "ws://localhost:8000/ws/playgame/"; 

    const chessSocket = new WebSocket(url);

    window.onbeforeunload = function() {
        chessSocket.close();
    }

    chessSocket.onmessage = function(e) {
        let data = JSON.parse(e.data);
        if(data["type"] == "state_notification") {
            chessBoard(); 
        }
    }
}

function chessBoard() {
    const content = document.getElementById("content");
    content.style = "position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);";
    content.innerHTML = '<div id="board1" style="width: 400px;"></div>';
    var config = {
        draggable: true,
        dropOffBoard: 'snapback',
        position: 'start',
        onDragStart: onDragStart,
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
    };
    board1 = Chessboard('board1', config);
}

window.onload = function() {
    socketConnect();
    chessBoard();
}

