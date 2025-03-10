import pygame.font
from pygame.sprite import Sprite

class Scoreboard(Sprite):
    """A class to report scoring information."""

    def __init__(self, br_game):
        super().__init__()
        self.screen = br_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = br_game.settings
        self.stats = br_game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        self.prep_score()

        self.prep_high_score()
        self.prep_level()
        self.prep_beers()


    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_beers(self):
        """Show how many packs of beers are left."""
        self.beers = pygame.sprite.Group()
        beer_pack = pygame.image.load(self.settings.health_image)
        for beers_number in range(self.stats.beers_left):
            img = Sprite()
            img.image = beer_pack
            img.rect = img.image.get_rect()
            img.rect.x = 10 + beers_number * img.rect.width
            img.rect.y = 10
            self.beers.add(img)


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        """Draw scores, level, and beers to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.beers.draw(self.screen)