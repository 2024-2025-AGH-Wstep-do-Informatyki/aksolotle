import os
import json # For the future

class ScoreSystem:
    def __init__(self, font, save_file="scores.json"): # Start scoring system
        self.score = 0
        self.font = font
        self.save_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', save_file)

    def add_points(self, points): # Add points to the current score
        self.score += points

    def reset_score(self): # Reset current score
        self.score = 0

    def save_score(self): # Save current score to the JSON file
        os.makedirs(os.path.dirname(self.save_file), exist_ok=True)
        with open(self.save_file, 'w') as file:
            file.write(str(self.score))

    def load_score(self): # Load recently saved score
        try:
            with open(self.save_file, 'r') as file:
                self.score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.score = 0

    def draw_score(self, screen, x, y): # Create and display score surface
        score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_surface, (x, y))