import pygame
from settings import *
from support import import_folder
from Entity import Entity
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_SPACE,
    K_m,
    K_q,
    K_e
)


class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, Destroy_attack, create_magic):
        super().__init__(groups)
        self.image = pygame.image.load("../Zelda Project/graphics/Player/Player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # Graphics setup
        self.import_player_assets()
        self.status = 'down_idle'

        # Movement
        self.attacking = False
        self.attack_cooldown = 200
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites

        # weapon selection
        self.create_attack = create_attack
        self.Destroy_attack = Destroy_attack
        self.weapon_index = 0
        self.weapon = list(Weapon_Data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration = 200

        # magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # stats
        self.stats = {'health': 100, 'attack': 10, 'magic': 80, 'speed': 9}
        self.health = self.stats['health']
        self.magic = self.stats['magic']
        self.exp = 123
        self.speed = self.stats['speed']

        # damage timer
        self.vulnerable = True
        self.hit_time = None
        self.invulnerable = 500

    def import_player_assets(self):
        character_path = '../Zelda Project/graphics/Player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        if keys[K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()

        if keys[K_m] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            style = list(magic_data.keys())[self.magic_index]
            strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
            cost = list(magic_data.values())[self.magic_index]['cost']
            self.create_magic(style, strength, cost)

        if keys[K_q] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()

            if self.weapon_index < len(list(Weapon_Data.keys())) - 1:
                self.weapon_index += 1
            else:
                self.weapon_index = 0

            self.weapon = list(Weapon_Data.keys())[self.weapon_index]

        if keys[K_e] and self.can_switch_magic:
            self.can_switch_magic = False
            self.magic_switch_time = pygame.time.get_ticks()

            if self.magic_index < len(list(magic_data.keys())) - 1:
                self.magic_index += 1
            else:
                self.magic_index = 0

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not ('idle' in self.status or 'attack' in self.status):
                self.status = self.status + "_idle"

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not ('attack' in self.status):
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + "_attack"
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + Weapon_Data[self.weapon]['cooldown']:
                self.attacking = False
                self.Destroy_attack()

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invulnerable:
                self.vulnerable = True

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration:
                self.can_switch_magic = True

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = Weapon_Data[self.weapon]['damage']
        return base_damage + weapon_damage

    def update(self):
        self.input()
        self.cooldown()
        self.get_status()
        self.animate()
        self.move(self.speed)
