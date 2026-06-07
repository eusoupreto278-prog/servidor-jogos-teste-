from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home_page():
    return '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portal de Jogos</title>
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: linear-gradient(135deg, #0b3d91, #1c6dd0); color: #fff; }
          header { padding: 24px 32px; text-align: center; }
          nav { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-top: 16px; }
          nav a { color: #fff; text-decoration: none; padding: 10px 18px; border: 1px solid rgba(255,255,255,0.5); border-radius: 8px; transition: background .2s ease; }
          nav a:hover { background: rgba(255,255,255,0.15); }
          .hero { max-width: 760px; margin: 0 auto; padding: 48px 24px; text-align: center; }
          .hero h1 { font-size: 3rem; margin-bottom: 12px; }
          .hero p { font-size: 1.1rem; line-height: 1.7; margin-bottom: 24px; }
          .buttons { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; }
          .button { display: inline-block; background: #ffd54f; color: #0b3d91; padding: 16px 28px; border-radius: 999px; text-decoration: none; font-weight: bold; }
          .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; padding: 24px; max-width: 960px; margin: 0 auto; }
          .card { background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.18); border-radius: 16px; padding: 20px; }
          .card h2 { margin-top: 0; }
          footer { text-align: center; padding: 20px; font-size: 0.95rem; opacity: 0.85; }
        </style>
      </head>
      <body>
        <header>
          <div class="hero">
            <h1>Bem-vindo ao Portal de Jogos</h1>
            <p>Escolha entre quatro jogos leves e divertidos: Cobrinha, Tetris, Pong e Tic Tac Toe. Todos funcionam no navegador do celular e do computador.</p>
            <div class="buttons">
              <a class="button" href="/game">Cobrinha</a>
              <a class="button" href="/tetris">Tetris</a>
              <a class="button" href="/pong">Pong</a>
              <a class="button" href="/tic-tac-toe">Tic Tac Toe</a>
            </div>
          </div>
          <nav>
            <a href="/">Início</a>
            <a href="/game">Cobrinha</a>
            <a href="/tetris">Tetris</a>
            <a href="/pong">Pong</a>
            <a href="/tic-tac-toe">Tic Tac Toe</a>
            <a href="/sobre">Sobre</a>
          </nav>
        </header>

        <section class="features">
          <div class="card">
            <h2>Cobrinha</h2>
            <p>Controles simples, swipe no celular e gráficos leves. Seu objetivo é crescer sem bater nas paredes ou em si mesmo.</p>
          </div>
          <div class="card">
            <h2>Tetris</h2>
            <p>Jogue Tetris com peças clássicas, gire e organize para completar linhas. Controles para desktop e mobile.</p>
          </div>
          <div class="card">
            <h2>Pong</h2>
            <p>Jogue Pong com controles simples e adversário de IA. Mova a raquete e rebata a bola para marcar pontos.</p>
          </div>
          <div class="card">
            <h2>Tic Tac Toe</h2>
            <p>Jogue uma partida rápida de Tic Tac Toe diretamente no navegador, com suporte para celular.</p>
          </div>
        </section>

        <footer>
          <p>Portal de jogos simples criado com Flask e HTML.</p>
        </footer>
      </body>
    </html>
    '''

@app.route('/sobre')
def sobre():
    return '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sobre o Site</title>
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: #0f243b; color: #f4f7fb; }
          .page { max-width: 760px; margin: 32px auto; padding: 24px; }
          a { color: #76c7ff; text-decoration: none; }
          a:hover { text-decoration: underline; }
          header { text-align: center; margin-bottom: 24px; }
          h1 { margin-bottom: 12px; }
          p { line-height: 1.7; }
        </style>
      </head>
      <body>
        <div class="page">
          <header>
            <h1>Sobre este site</h1>
            <p>Um site simples em Flask que serve como portal para os jogos da cobrinha e do Tetris.</p>
          </header>
          <p>Esta página foi criada para oferecer uma experiência leve e acessível em qualquer navegador. A partir daqui você pode acessar ambos os jogos e se divertir enquanto aprende.</p>
          <p><a href="/">Voltar para a página inicial</a></p>
        </div>
      </body>
    </html>
    '''

@app.route('/tetris')
def tetris_page():
    return '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Tetris</title>
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: #111827; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
          .game-wrapper { width: 100%; max-width: 360px; padding: 16px; box-sizing: border-box; text-align: center; }
          canvas { background: #111827; border: 4px solid #38bdf8; border-radius: 12px; width: 100%; height: auto; display: block; margin: 0 auto; }
          .info { margin-top: 16px; font-size: 16px; line-height: 1.6; }
          .info div { margin: 8px 0; }
          .button, .control-button { margin-top: 12px; padding: 12px 18px; background: #38bdf8; border: none; color: #111827; border-radius: 8px; cursor: pointer; font-size: 16px; }
          .button:hover, .control-button:hover { background: #0ea5e9; }
          .nav { margin-top: 18px; }
          .nav a { color: #93c5fd; text-decoration: none; margin: 0 8px; }
          .nav a:hover { text-decoration: underline; }
          .controls { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 16px; }
          .controls button { min-height: 48px; }
          @media (max-width: 420px) {
            .button, .control-button { width: 100%; }
          }
        </style>
      </head>
      <body>
        <div class="game-wrapper">
          <h1>Tetris</h1>
          <canvas id="tetrisCanvas" width="300" height="600"></canvas>
          <div class="info">
            <div>Pontuação: <strong id="score">0</strong></div>
            <div>Status: <strong id="status">Use as setas ou botões</strong></div>
          </div>
          <button class="button" onclick="resetGame()">Reiniciar</button>
          <div class="controls">
            <button class="control-button" onclick="moveLeft()">Esquerda</button>
            <button class="control-button" onclick="rotatePiece()">Rodar</button>
            <button class="control-button" onclick="moveRight()">Direita</button>
            <button class="control-button" onclick="softDrop()">Descer</button>
          </div>
          <div class="nav">
            <a href="/">Início</a> | <a href="/game">Cobrinha</a> | <a href="/pong">Pong</a> | <a href="/tic-tac-toe">Tic Tac Toe</a> | <a href="/sobre">Sobre</a>
          </div>
        </div>

        <script>
          const canvas = document.getElementById('tetrisCanvas');
          const ctx = canvas.getContext('2d');
          const cols = 10;
          const rows = 20;
          const blockSize = 30;
          const emptyColor = '#0f172a';
          const pieces = [
            { color: '#ef4444', shape: [[1,1,1,1]] },
            { color: '#f97316', shape: [[1,1,1],[1,0,0]] },
            { color: '#eab308', shape: [[1,1,1],[0,0,1]] },
            { color: '#22c55e', shape: [[1,1,0],[0,1,1]] },
            { color: '#38bdf8', shape: [[0,1,1],[1,1,0]] },
            { color: '#a855f7', shape: [[1,1],[1,1]] },
            { color: '#8b5cf6', shape: [[1,1,1],[0,1,0]] }
          ];

          let board = [];
          let currentPiece = null;
          let currentX = 0;
          let currentY = 0;
          let dropInterval = 600;
          let dropTimer = null;
          let score = 0;
          let gameOver = false;
          const scoreEl = document.getElementById('score');
          const statusEl = document.getElementById('status');

          function createBoard() {
            board = Array.from({ length: rows }, () => Array(cols).fill(emptyColor));
          }

          function drawCell(x, y, color) {
            ctx.fillStyle = color;
            ctx.fillRect(x * blockSize, y * blockSize, blockSize - 2, blockSize - 2);
          }

          function drawBoard() {
            ctx.fillStyle = '#0f172a';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            for (let y = 0; y < rows; y += 1) {
              for (let x = 0; x < cols; x += 1) {
                drawCell(x, y, board[y][x]);
              }
            }
          }

          function drawPiece(piece, offsetX, offsetY) {
            piece.shape.forEach((row, y) => {
              row.forEach((value, x) => {
                if (value) {
                  drawCell(offsetX + x, offsetY + y, piece.color);
                }
              });
            });
          }

          function randomPiece() {
            const index = Math.floor(Math.random() * pieces.length);
            return JSON.parse(JSON.stringify(pieces[index]));
          }

          function placePiece() {
            currentPiece.shape.forEach((row, y) => {
              row.forEach((value, x) => {
                if (value) {
                  board[currentY + y][currentX + x] = currentPiece.color;
                }
              });
            });
          }

          function collision(xOffset, yOffset, piece) {
            const shape = piece.shape;
            for (let y = 0; y < shape.length; y += 1) {
              for (let x = 0; x < shape[y].length; x += 1) {
                if (shape[y][x]) {
                  const px = currentX + x + xOffset;
                  const py = currentY + y + yOffset;
                  if (px < 0 || px >= cols || py >= rows || (py >= 0 && board[py][px] !== emptyColor)) {
                    return true;
                  }
                }
              }
            }
            return false;
          }

          function rotate(piece) {
            const shape = piece.shape;
            const rotated = shape[0].map((_, index) => shape.map(row => row[index]).reverse());
            return { ...piece, shape: rotated };
          }

          function clearLines() {
            let linesCleared = 0;
            board = board.filter(row => row.some(cell => cell === emptyColor));
            linesCleared = rows - board.length;
            while (board.length < rows) {
              board.unshift(Array(cols).fill(emptyColor));
            }
            if (linesCleared > 0) {
              score += linesCleared * 10;
              scoreEl.textContent = score;
              statusEl.textContent = `Você limpou ${linesCleared} linha(s)!`;
            }
          }

          function dropPiece() {
            if (!collision(0, 1, currentPiece)) {
              currentY += 1;
            } else {
              placePiece();
              clearLines();
              spawnPiece();
            }
          }

          function spawnPiece() {
            currentPiece = randomPiece();
            currentX = Math.floor((cols - currentPiece.shape[0].length) / 2);
            currentY = -1;
            if (collision(0, 0, currentPiece)) {
              gameOver = true;
              statusEl.textContent = 'Game over! Toque em Reiniciar.';
              clearInterval(dropTimer);
            }
          }

          function move(offsetX) {
            if (gameOver) return;
            if (!collision(offsetX, 0, currentPiece)) {
              currentX += offsetX;
            }
          }

          function moveLeft() { move(-1); }
          function moveRight() { move(1); }
          function softDrop() { if (!collision(0, 1, currentPiece)) { currentY += 1; } }

          function rotatePiece() {
            const rotated = rotate(currentPiece);
            if (!collision(0, 0, rotated)) {
              currentPiece = rotated;
            }
          }

          document.addEventListener('keydown', (event) => {
            if (gameOver) return;
            if (event.key === 'ArrowLeft') moveLeft();
            if (event.key === 'ArrowRight') moveRight();
            if (event.key === 'ArrowDown') softDrop();
            if (event.key === 'ArrowUp') rotatePiece();
          });

          function gameLoop() {
            if (!gameOver) {
              dropPiece();
              drawBoard();
              drawPiece(currentPiece, currentX, currentY);
            }
          }

          function resetGame() {
            gameOver = false;
            score = 0;
            scoreEl.textContent = score;
            statusEl.textContent = 'Use as setas ou botões';
            createBoard();
            spawnPiece();
            if (dropTimer) clearInterval(dropTimer);
            dropTimer = setInterval(gameLoop, dropInterval);
            drawBoard();
            drawPiece(currentPiece, currentX, currentY);
          }

          resetGame();
        </script>
      </body>
    </html>
    '''

@app.route('/pong')
def pong_page():
    return '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Pong</title>
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: #081b29; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
          .game-wrapper { width: 100%; max-width: 380px; padding: 16px; text-align: center; box-sizing: border-box; }
          canvas { width: 100%; height: auto; background: #0f172a; border: 4px solid #38bdf8; border-radius: 12px; display: block; margin: 0 auto; }
          .info { margin-top: 16px; font-size: 16px; line-height: 1.6; }
          .button, .control-button { margin-top: 12px; padding: 12px 18px; background: #38bdf8; border: none; color: #111827; border-radius: 8px; cursor: pointer; font-size: 16px; }
          .button:hover, .control-button:hover { background: #0ea5e9; }
          .controls { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 16px; }
          .controls button { min-width: 100px; }
          .nav { margin-top: 18px; }
          .nav a { color: #93c5fd; text-decoration: none; margin: 0 8px; }
          .nav a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <div class="game-wrapper">
          <h1>Pong</h1>
          <canvas id="pongCanvas" width="320" height="240"></canvas>
          <div class="info">
            <div>Pontuação: <strong id="score">0</strong></div>
            <div>Status: <strong id="status">Use as setas ou botões</strong></div>
          </div>
          <button class="button" onclick="resetGame()">Reiniciar</button>
          <div class="controls">
            <button class="control-button" onclick="movePlayer(-1)">Esquerda</button>
            <button class="control-button" onclick="movePlayer(1)">Direita</button>
          </div>
          <div class="nav">
            <a href="/">Início</a> | <a href="/game">Cobrinha</a> | <a href="/tetris">Tetris</a> | <a href="/tic-tac-toe">Tic Tac Toe</a> | <a href="/sobre">Sobre</a>
          </div>
        </div>

        <script>
          const canvas = document.getElementById('pongCanvas');
          const ctx = canvas.getContext('2d');
          const paddleWidth = 80;
          const paddleHeight = 10;
          const ballRadius = 6;
          let playerX = (canvas.width - paddleWidth) / 2;
          let aiX = (canvas.width - paddleWidth) / 2;
          let ballX = canvas.width / 2;
          let ballY = canvas.height / 2;
          let ballSpeedX = 0;
          let ballSpeedY = 0;
          let score = 0;
          let gameOver = false;
          let ballStarted = false;
          let startTimer = null;
          let playerSpeed = 25;
          let playerVelocity = 0;
          let leftPressed = false;
          let rightPressed = false;
          const scoreEl = document.getElementById('score');
          const statusEl = document.getElementById('status');

          function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawBoard();
            drawPaddle(playerX, canvas.height - paddleHeight - 10);
            drawPaddle(aiX, 10);
            drawBall();
            if (!gameOver) {
              update();
            }
          }

          function drawBoard() {
            ctx.fillStyle = '#0f172a';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
          }

          function drawPaddle(x, y) {
            ctx.fillStyle = '#38bdf8';
            ctx.fillRect(x, y, paddleWidth, paddleHeight);
          }

          function drawBall() {
            ctx.fillStyle = '#facc15';
            ctx.beginPath();
            ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2);
            ctx.fill();
          }

          function update() {
            updatePlayer();
            ballX += ballSpeedX;
            ballY += ballSpeedY;

            if (ballX - ballRadius < 0 || ballX + ballRadius > canvas.width) {
              ballSpeedX = -ballSpeedX;
            }

            const topPaddleY = 10;
            const bottomPaddleY = canvas.height - paddleHeight - 10;

            if (ballSpeedY < 0 && ballY - ballRadius <= topPaddleY + paddleHeight) {
              if (ballX >= aiX && ballX <= aiX + paddleWidth) {
                ballSpeedY = -ballSpeedY;
              } else if (ballY - ballRadius <= 0) {
                ballSpeedY = -ballSpeedY;
              }
            }

            if (ballSpeedY > 0 && ballY + ballRadius >= bottomPaddleY) {
              if (ballX >= playerX && ballX <= playerX + paddleWidth) {
                ballSpeedY = -ballSpeedY;
                score += 1;
                scoreEl.textContent = score;
                statusEl.textContent = 'Boa! Continue.';
              } else if (ballY + ballRadius > canvas.height) {
                endGame();
              }
            }

            aiX += (ballX - (aiX + paddleWidth / 2)) * 0.05;
            aiX = Math.max(0, Math.min(canvas.width - paddleWidth, aiX));
          }

          function startBall() {
            if (ballStarted || gameOver) return;
            ballStarted = true;
            startTimer = setTimeout(() => {
              ballSpeedX = Math.random() < 0.5 ? 2.0 : -2.0;
              ballSpeedY = -2.0;
              statusEl.textContent = 'Bola em movimento!';
            }, 500);
          }

          function updatePlayer() {
            if (leftPressed) {
              playerVelocity = -playerSpeed;
            } else if (rightPressed) {
              playerVelocity = playerSpeed;
            } else {
              playerVelocity = 0;
            }
            playerX += playerVelocity;
            playerX = Math.max(0, Math.min(canvas.width - paddleWidth, playerX));
          }

          function movePlayer(direction) {
            if (gameOver) return;
            playerX += direction * playerSpeed;
            playerX = Math.max(0, Math.min(canvas.width - paddleWidth, playerX));
            if (!ballStarted) {
              startBall();
            }
          }

          function endGame() {
            gameOver = true;
            if (startTimer) {
              clearTimeout(startTimer);
              startTimer = null;
            }
            statusEl.textContent = 'Fim de jogo! Toque em Reiniciar.';
          }

          function resetGame() {
            gameOver = false;
            playerX = (canvas.width - paddleWidth) / 2;
            aiX = (canvas.width - paddleWidth) / 2;
            ballX = canvas.width / 2;
            ballY = canvas.height / 2;
            ballSpeedX = 0;
            ballSpeedY = 0;
            ballStarted = false;
            if (startTimer) {
              clearTimeout(startTimer);
              startTimer = null;
            }
            score = 0;
            scoreEl.textContent = score;
            statusEl.textContent = 'Use as setas ou botões. Mova para iniciar.';
          }

          document.addEventListener('keydown', (event) => {
            if (event.key === 'ArrowLeft') {
              leftPressed = true;
              if (!ballStarted) startBall();
            }
            if (event.key === 'ArrowRight') {
              rightPressed = true;
              if (!ballStarted) startBall();
            }
          });

          document.addEventListener('keyup', (event) => {
            if (event.key === 'ArrowLeft') leftPressed = false;
            if (event.key === 'ArrowRight') rightPressed = false;
          });

          setInterval(draw, 16);
          resetGame();
        </script>
      </body>
    </html>
    '''

@app.route('/tic-tac-toe')
def tic_tac_toe_page():
    return '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tic Tac Toe</title>
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: #0f172a; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
          .game-wrapper { width: 100%; max-width: 360px; padding: 16px; text-align: center; box-sizing: border-box; }
          .board { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 16px; }
          .cell { width: 100%; height: 100px; font-size: 2rem; font-weight: bold; color: #111827; background: #e2e8f0; border: none; border-radius: 12px; cursor: pointer; }
          .info { margin-top: 16px; font-size: 16px; line-height: 1.6; }
          .button { margin-top: 16px; padding: 12px 18px; background: #38bdf8; border: none; color: #111827; border-radius: 8px; cursor: pointer; font-size: 16px; }
          .button:hover { background: #0ea5e9; }
          .nav { margin-top: 18px; }
          .nav a { color: #93c5fd; text-decoration: none; margin: 0 8px; }
          .nav a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <div class="game-wrapper">
          <h1>Tic Tac Toe</h1>
          <div class="info">Jogador atual: <strong id="currentPlayer">X</strong></div>
          <div class="board" id="board">
            <button class="cell" onclick="makeMove(0)"></button>
            <button class="cell" onclick="makeMove(1)"></button>
            <button class="cell" onclick="makeMove(2)"></button>
            <button class="cell" onclick="makeMove(3)"></button>
            <button class="cell" onclick="makeMove(4)"></button>
            <button class="cell" onclick="makeMove(5)"></button>
            <button class="cell" onclick="makeMove(6)"></button>
            <button class="cell" onclick="makeMove(7)"></button>
            <button class="cell" onclick="makeMove(8)"></button>
          </div>
          <div class="info"><span id="status">Vez de X</span></div>
          <button class="button" onclick="resetGame()">Reiniciar</button>
          <div class="nav">
            <a href="/">Início</a> | <a href="/game">Cobrinha</a> | <a href="/tetris">Tetris</a> | <a href="/pong">Pong</a> | <a href="/sobre">Sobre</a>
          </div>
        </div>

        <script>
          let boardState = Array(9).fill('');
          let currentPlayer = 'X';
          let gameOver = false;
          const currentPlayerEl = document.getElementById('currentPlayer');
          const statusEl = document.getElementById('status');
          const cells = Array.from(document.querySelectorAll('.cell'));

          function updateBoard() {
            cells.forEach((cell, index) => {
              cell.textContent = boardState[index];
            });
            currentPlayerEl.textContent = currentPlayer;
          }

          function makeMove(index) {
            if (gameOver || boardState[index]) return;
            boardState[index] = currentPlayer;
            updateBoard();
            if (checkWinner()) {
              statusEl.textContent = currentPlayer + ' venceu!';
              gameOver = true;
              return;
            }
            if (boardState.every(cell => cell)) {
              statusEl.textContent = 'Empate!';
              gameOver = true;
              return;
            }
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            statusEl.textContent = 'Vez de ' + currentPlayer;
          }

          function checkWinner() {
            const winLines = [
              [0,1,2], [3,4,5], [6,7,8],
              [0,3,6], [1,4,7], [2,5,8],
              [0,4,8], [2,4,6]
            ];
            return winLines.some(([a,b,c]) => {
              return boardState[a] && boardState[a] === boardState[b] && boardState[a] === boardState[c];
            });
          }

          function resetGame() {
            boardState = Array(9).fill('');
            currentPlayer = 'X';
            gameOver = false;
            statusEl.textContent = 'Vez de X';
            updateBoard();
          }

          resetGame();
        </script>
      </body>
    </html>
    '''

@app.route('/game')
def game_page():
    return '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Jogo da Cobrinha</title>
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: #081b29; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
          .game-wrapper { text-align: center; width: 100%; max-width: 520px; padding: 16px; box-sizing: border-box; }
          canvas { background: #0f2d4b; border: 4px solid #28a745; border-radius: 12px; display: block; margin: 0 auto; width: 100%; max-width: 400px; height: auto; touch-action: none; }
          .info { margin-top: 18px; font-size: 18px; }
          .info span { display: inline-block; min-width: 120px; }
          .button, .control-button { margin-top: 16px; padding: 12px 18px; background: #28a745; border: none; color: #fff; border-radius: 8px; cursor: pointer; font-size: 16px; }
          .button:hover, .control-button:hover { background: #1f8f3c; }
          .nav { margin-top: 20px; }
          .nav a { color: #76c7ff; text-decoration: none; margin: 0 10px; }
          .nav a:hover { text-decoration: underline; }
          .controls { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 320px; margin: 20px auto 0; }
          .controls button { min-height: 52px; }
          .controls .empty { visibility: hidden; }
          @media (max-width: 420px) {
            .game-wrapper { padding: 12px; }
            .info { font-size: 16px; }
            .button, .control-button { width: 100%; }
            .controls { gap: 10px; }
          }
        </style>
      </head>
      <body>
        <div class="game-wrapper">
          <h1>Jogo da Cobrinha</h1>
          <canvas id="gameCanvas" width="400" height="400"></canvas>
          <div class="info">
            <div><span>Pontuação:</span><strong id="score">0</strong></div>
            <div><span>Status:</span><strong id="status">Use setas, botões ou swipe</strong></div>
          </div>
          <button class="button" onclick="resetGame()">Reiniciar</button>
          <div class="controls">
            <button class="control-button" onclick="setDirection(0, -1)">Cima</button>
            <button class="control-button empty">.</button>
            <button class="control-button" onclick="setDirection(0, 1)">Baixo</button>
            <button class="control-button" onclick="setDirection(-1, 0)">Esquerda</button>
            <button class="control-button empty">.</button>
            <button class="control-button" onclick="setDirection(1, 0)">Direita</button>
          </div>
          <div class="nav">
            <a href="/">Início</a> | <a href="/tetris">Tetris</a> | <a href="/pong">Pong</a> | <a href="/tic-tac-toe">Tic Tac Toe</a> | <a href="/sobre">Sobre</a>
          </div>
        </div>

        <script>
          const canvas = document.getElementById('gameCanvas');
          const ctx = canvas.getContext('2d');
          const gridSize = 20;
          const tileCount = 20;
          let snake = [{ x: 10, y: 10 }];
          let velocity = { x: 0, y: 0 };
          let apple = { x: 15, y: 15 };
          let score = 0;
          let gameOver = false;
          let touchStartX = 0;
          let touchStartY = 0;
          const scoreEl = document.getElementById('score');
          const statusEl = document.getElementById('status');

          function draw() {
            if (gameOver) {
              ctx.fillStyle = '#081b29';
              ctx.fillRect(0, 0, canvas.width, canvas.height);
              ctx.fillStyle = '#ff4d4d';
              ctx.font = '22px Arial';
              ctx.textAlign = 'center';
              ctx.fillText('Fim de jogo! Pressione Reiniciar.', canvas.width / 2, canvas.height / 2);
              return;
            }

            updateSnake();
            checkCollisions();
            drawBoard();
            drawApple();
            drawSnake();
          }

          function updateSnake() {
            const head = { x: snake[0].x + velocity.x, y: snake[0].y + velocity.y };
            snake.unshift(head);
            if (head.x === apple.x && head.y === apple.y) {
              score += 1;
              scoreEl.textContent = score;
              placeApple();
              statusEl.textContent = 'Ótimo! Continue.';
            } else {
              snake.pop();
            }
          }

          function checkCollisions() {
            const head = snake[0];
            if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
              endGame();
            }
            for (let i = 1; i < snake.length; i += 1) {
              if (head.x === snake[i].x && head.y === snake[i].y) {
                endGame();
              }
            }
          }

          function drawBoard() {
            ctx.fillStyle = '#081b29';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
          }

          function drawSnake() {
            snake.forEach((segment, index) => {
              ctx.fillStyle = index === 0 ? '#b2ffcc' : '#00d66a';
              ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
            });
          }

          function drawApple() {
            ctx.fillStyle = '#ff4d4d';
            ctx.fillRect(apple.x * gridSize, apple.y * gridSize, gridSize - 2, gridSize - 2);
          }

          function placeApple() {
            apple = {
              x: Math.floor(Math.random() * tileCount),
              y: Math.floor(Math.random() * tileCount),
            };
            if (snake.some(segment => segment.x === apple.x && segment.y === apple.y)) {
              placeApple();
            }
          }

          function endGame() {
            gameOver = true;
            statusEl.textContent = 'Game over! Reinicie para jogar novamente.';
            velocity = { x: 0, y: 0 };
          }

          function resetGame() {
            snake = [{ x: 10, y: 10 }];
            velocity = { x: 0, y: 0 };
            placeApple();
            score = 0;
            gameOver = false;
            scoreEl.textContent = score;
            statusEl.textContent = 'Use setas, botões ou swipe';
          }

          function setDirection(x, y) {
            if (gameOver) return;
            if (x === 0 && y === -1 && velocity.y === 0) {
              velocity = { x: 0, y: -1 };
            }
            if (x === 0 && y === 1 && velocity.y === 0) {
              velocity = { x: 0, y: 1 };
            }
            if (x === -1 && y === 0 && velocity.x === 0) {
              velocity = { x: -1, y: 0 };
            }
            if (x === 1 && y === 0 && velocity.x === 0) {
              velocity = { x: 1, y: 0 };
            }
          }

          document.addEventListener('keydown', (event) => {
            if (gameOver) return;
            if (event.key === 'ArrowUp') setDirection(0, -1);
            if (event.key === 'ArrowDown') setDirection(0, 1);
            if (event.key === 'ArrowLeft') setDirection(-1, 0);
            if (event.key === 'ArrowRight') setDirection(1, 0);
          });

          canvas.addEventListener('touchstart', (event) => {
            const touch = event.changedTouches[0];
            touchStartX = touch.clientX;
            touchStartY = touch.clientY;
          }, { passive: true });

          canvas.addEventListener('touchend', (event) => {
            const touch = event.changedTouches[0];
            const deltaX = touch.clientX - touchStartX;
            const deltaY = touch.clientY - touchStartY;
            const threshold = 30;
            if (Math.abs(deltaX) > Math.abs(deltaY)) {
              if (deltaX > threshold) setDirection(1, 0);
              else if (deltaX < -threshold) setDirection(-1, 0);
            } else {
              if (deltaY > threshold) setDirection(0, 1);
              else if (deltaY < -threshold) setDirection(0, -1);
            }
          }, { passive: true });

          function resizeCanvas() {
            const size = Math.min(window.innerWidth - 32, 400);
            canvas.style.width = size + 'px';
            canvas.style.height = size + 'px';
          }

          window.addEventListener('resize', resizeCanvas);
          resetGame();
          resizeCanvas();
          setInterval(draw, 120);
        </script>
      </body>
    </html>
    '''

app.run(host="0.0.0.0", port=5000)