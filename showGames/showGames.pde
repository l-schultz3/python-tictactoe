String[] games;

int i = 0;

void setup() {
  games = loadStrings("gameFile.txt");
  print(games.length);
  
  size(600, 600); 
  textSize(120);
}

void draw() {
  background(0);
  strokeWeight(2);
  stroke(255, 0, 0);
  line(0, 100, 300, 100);
  line(0, 200, 300, 200);
  line(100, 0, 100, 300);
  line(200, 0, 200, 300);
  stroke(0, 0, 255);
  line(300, 100, 600, 100);
  line(300, 200, 600, 200);
  line(400, 0, 400, 300);
  line(500, 0, 500, 300);
  
  stroke(0, 255, 0);
  line(0, 400, 300, 400);
  line(0, 500, 300, 500);
  line(100, 300, 100, 600);
  line(200, 300, 200, 600);
  stroke(255, 255, 0);
  line(300, 400, 600, 400);
  line(300, 500, 600, 500);
  line(400, 300, 400, 600);
  line(500, 300, 500, 600);
  
  
  strokeWeight(4);
  stroke(255);
  line(300, 0, 300, 600);
  line(0, 300, 600, 300);

  showGame(games[i], 5, 95);
  showGame(games[i], 305, 95);
  showGame(games[i], 5, 395);
  showGame(games[i], 305, 395);

  waiting();
}

void showGame(String game, int startX, int startY) {
  for (int j = 0; j < 9; j++) {
    if (game.charAt(j) == '1') {
      text("X", ((j % 3) * 100) + startX, (floor(j / 3) * 100) + startY);
    } else if (game.charAt(j) == '0') {
      text("O", ((j % 3) * 100) + startX, (floor(j / 3) * 100) + startY);
    }
  }
  
  if (i < games.length - 1) {
    i++;
  }
}

void waiting() {
  int waitFor = millis() + 1000;

  while (millis() < waitFor) {
  }
}
