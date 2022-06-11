import pygame
from settings import *


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, FONT_SIZE)

        # bar setup
        self.HEALTH_BAR = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.MAGIC_BAR = pygame.Rect(10, 34, MAGIC_BAR_WIDTH, BAR_HEIGHT)

        # weapon stuff
        self.weapon_graphics = []
        for weapon in Weapon_Data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        # magic stuff
        self.magic_graphics = []
        for magic in magic_data.values():
            path = magic['graphic']
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG, bg_rect)

        # convert the stats to pixels
        ratio = current/max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # draw the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG, text_rect.inflate(7, 3))
        pygame.draw.rect(self.display_surface, UI_BORDER, text_rect.inflate(7, 3), 3)
        self.display_surface.blit(text_surf, text_rect)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX, ITEM_BOX)
        pygame.draw.rect(self.display_surface, UI_BG, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_ACTIVE_BORDER, bg_rect, 5)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER, bg_rect, 5)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(35, 555, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(weapon_surf, weapon_rect)

    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(128, 590, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(magic_surf, magic_rect)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.HEALTH_BAR, HEALTH)
        self.show_bar(player.magic, player.stats['magic'], self.MAGIC_BAR, MAGIC)

        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)

