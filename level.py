import pygame.image
from settings import *
from tile import Tile
from player import Player
from weapons import Weapon
from ui import UI
from support import *
from enemy import Enemy
from random import choice
from particles import AnimationPlayer


class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack stuff
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

        # UI
        self.ui = UI()

        # particles
        self.animation_player = AnimationPlayer()

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hit_time = pygame.time.get_ticks()
            # spawn particles

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_magic(self, style, strength, cost):
        pass

    def create_map(self):
        layouts = {
            'object': import_csv_layout('../Zelda Project/graphics/map/csv files/untitled._Big objects.csv'),
            'boundary': import_csv_layout('../Zelda Project/graphics/map/csv files/untitled._Border Blocks.csv'),
            'grass': import_csv_layout('../Zelda Project/graphics/map/csv files/untitled._Objects.csv'),
            'entities': import_csv_layout('../Zelda Project/graphics/map/csv files/untitled._Entities.csv')
        }
        graphics = {
            'grass': import_folder('../Zelda Project/graphics/map/grass'),
            'objects': import_folder('../Zelda Project/graphics/map/objects')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y),
                            [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

                        if style == 'entities':
                            if col == '48':
                                self.player = Player((x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)
                            else:
                                if col == '28':
                                    monster_name = 'beast'
                                elif col == '8':
                                    monster_name = 'mollusc'
                                elif col == '20':
                                    monster_name = 'giantflame'
                                elif col == '26':
                                    monster_name = 'dragon'
                                elif col == '44':
                                    monster_name = 'skull'
                                Enemy(monster_name, (x, y), [self.visible_sprites, self.attackable_sprites],
                                self.obstacle_sprites, self.damage_player)

    def run(self):
        # update and draw the game
        self.visible_sprites.Custom_Draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)
        self.player_attack_logic()
        # debug()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_image = pygame.image.load('../Zelda Project/graphics/map/untitled.png').convert()
        self.floor_rect = self.floor_image.get_rect(topleft=(0, 0))

    def Custom_Draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_image, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
