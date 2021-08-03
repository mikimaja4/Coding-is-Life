import pygame
class health:
    def __init__(self):
        super().__init__()
        self.current_health = 200
        self.maximum_health = 999
        self.health_bar_length = 150
        self.health_ratio = self.maximum_health / self.health_bar_length

    def update(self, screen):
        self.basic_health(screen)

    def take_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def get_health(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health

    def basic_health(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.health_bar_length, 25), 4)
        font = pygame.font.Font(None, 36)
        current_text = str(self.current_health)
        current = font.render(current_text, False, (0, 0, 0))
        screen.blit(current, (10, 40))

        slash = font.render('/', False, (0, 0, 0))
        screen.blit(slash, (55, 40))

        max_text = str(self.maximum_health)
        max = font.render(max_text, False, (0, 0, 0))
        screen.blit(max, (68, 40))
