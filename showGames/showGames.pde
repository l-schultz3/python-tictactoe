String[] games;

int i = 0;

void setup() {
  games = loadStrings("gameFile.txt");
  
  size(300, 300); 
  textSize(120);
}

void draw() {
  background(0);
  stroke(255);
  line(0, 100, 300, 100);
  line(0, 200, 300, 200);
  line(100, 0, 100, 300);
  line(200, 0, 200, 300);

  if (games[i].charAt(0) == '1') {
    text("X", 5, 95);
  } else if (games[i].charAt(0) == '0') {
    text("O", 5, 95);
  }

  if (games[i].charAt(1) == '1') {
    text("X", 105, 95);
  } else if (games[i].charAt(1) == '0') {
    text("O", 105, 95);
  }

  if (games[i].charAt(2) == '1') {
    text("X", 205, 95);
  } else if (games[i].charAt(2) == '0') {
    text("O", 205, 95);
  }
  
  if (games[i].charAt(3) == '1') {
    text("X", 5, 195);
  } else if (games[i].charAt(3) == '0') {
    text("O", 5, 195);
  }
  
  if (games[i].charAt(4) == '1') {
    text("X", 105, 195);
  } else if (games[i].charAt(4) == '0') {
    text("O", 105, 195);
  }
  
  if (games[i].charAt(5) == '1') {
    text("X", 205, 195);
  } else if (games[i].charAt(5) == '0') {
    text("O", 205, 195);
  }
  
  if (games[i].charAt(6) == '1') {
    text("X", 5, 295);
  } else if (games[i].charAt(6) == '0') {
    text("O", 5, 295);
  }
  
  if (games[i].charAt(7) == '1') {
    text("X", 105, 295);
  } else if (games[i].charAt(7) == '0') {
    text("O", 105, 295);
  }
  
  if (games[i].charAt(8) == '1') {
    text("X", 205, 295);
  } else if (games[i].charAt(8) == '0') {
    text("O", 205, 295);
  }

  waiting();
  
  if (i < games.length - 1) {
    i++;
  }
}

void waiting() {
  int waitFor = millis() + 0;

  while (millis() < waitFor) {
  }
}
