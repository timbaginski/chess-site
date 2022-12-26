function socketConnect() {
    let url = "ws://localhost:8000/ws/playgame/"; 

    const chessSocket = new WebSocket(url);

    chessSocket.onmessage = function(e) {
        let data = JSON.parse(e.data);
        console.log('Data: ', data);
    }
}

socketConnect();