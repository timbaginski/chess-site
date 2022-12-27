function socketConnect() {
    let url = "ws://localhost:8000/ws/playgame/"; 

    const chessSocket = new WebSocket(url);

    chessSocket.onmessage = function(e) {
        let data = JSON.parse(e.data);
        if(data["type"] == "state_notification") {
            chessBoard(); 
        }
    }
}

function chessBoard() {
    var board1 = Chessboard('board1', 'start');
}

socketConnect();