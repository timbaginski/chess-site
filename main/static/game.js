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
    content.innerHTML = '<div id="board1" style="width: 400px"></div>';
    var board1 = Chessboard('board1', 'start');
}

window.onload = function() {
    socketConnect();
    chessBoard();
}

