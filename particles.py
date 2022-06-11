import pygame
from support import import_folder


class AnimationPlayer:
    def __int__(self):
        super().__init__()
        self.frames = {
            # magic particles
            'flame': import_folder('../Zelda Project/graphics/particles/'),
            'aura': import_folder('../Zelda Project/graphics/particles/'),
            'heal': import_folder('../Zelda Project/graphics/particles/'),

            # attacks
            'fire_attack': import_folder('../Zelda Project/graphics/particles/enemy attacks/fire_attack'),
            'leaf_attack': import_folder('../Zelda Project/graphics/particles/leaf_attack'),
            'claw': import_folder('../Zelda Project/graphics/particles/claw'),

            # monster deaths
            'bigflame': import_folder('../Zelda Project/graphics/particles/death/bigflame death'),
            'skull': import_folder('../Zelda Project/graphics/particles/death/skull death'),
            'dragon': import_folder('../Zelda Project/graphics/particles/death/dragon death'),
            'beast': import_folder('../Zelda Project/graphics/particles/death/beast death'),
            'mollusc': import_folder('../Zelda Project/graphics/particles/death/mollusc death'),

            # leaves
            'leaf': import_folder('../Zelda Project/graphics/particles/leaves'),
        }

    def create_grass_particles(self, pos, groups):
        animation_frames = self.frames['leaf']
        ParticleEffects(pos, animation_frames, groups)


class ParticleEffects(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames) - 1:
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()