WIDTH = 1280
HEIGHT = 720
FPS = 30
TILE_SIZE = 64

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 400
MAGIC_BAR_WIDTH = 180
ITEM_BOX = 120
UI_FONT = 'graphics/font/UI FONT.ttf'
FONT_SIZE = 24

# general colours
WATER = '#71ddee'
UI_BG = '#222222'
UI_BORDER = '#111111'
TEXT = '#EEEEEE'

# UI colours
HEALTH = 'red'
MAGIC = 'blue'
UI_ACTIVE_BORDER = 'gold'

# Weapon data
Weapon_Data = {
    'Big sword': {'cooldown': 250, 'damage': 50, 'graphic': '../Zelda Project/graphics/Weapons/Big sword/full.png'},
    'Spear': {'cooldown': 400, 'damage': 70, 'graphic': '../Zelda Project/graphics/Weapons/Spear/full.png'},
    'Sai': {'cooldown': 15, 'damage': 20, 'graphic': '../Zelda Project/graphics/Weapons/Sai/full.png'},
}

magic_data = {
    'heal': {'strength': 25, 'cost': 10, 'graphic': '../Zelda Project/graphics/magic/magic1.png'},
    'flame': {'strength': 50, 'cost': 25, 'graphic': '../Zelda Project/graphics/magic/magic2.png'}
}

# Monster Data
Monster_Data = {
    'beast': {'health': 300, 'exp': 15, 'damage': 25, 'attack_type': 'claw', 'speed': 5, 'knockback': 7, 'attack_radius': 65, 'notice_radius': 200},
    'mollusc': {'health': 150, 'exp': 15, 'damage': 12, 'attack_type': 'claw', 'speed': 3, 'knockback': 3, 'attack_radius': 50, 'notice_radius': 300},
    'giantflame': {'health': 500, 'exp': 1500, 'damage': 50, 'attack_type': 'fire_attack', 'speed': 6, 'knockback': 3, 'attack_radius': 120, 'notice_radius': 250},
    'dragon': {'health': 200, 'exp': 15, 'damage': 17, 'attack_type': 'leaf_attack', 'speed': 4, 'knockback': 3, 'attack_radius': 80, 'notice_radius': 500},
    'skull': {'health': 75, 'exp': 15, 'damage': 10, 'attack_type': 'claw', 'speed': 7, 'knockback': 3, 'attack_radius': 75, 'notice_radius': 500}
}

World_Map = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', 'x'],
    ['x', ' ', 'p', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', ' ', ' ', 'x', ' ', 'e', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', 'x'],
    ['x', 'e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ]
