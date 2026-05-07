import os
from pathlib import Path
import pygame
import random
from src.towers.tower import Tower, TARGETING_LABELS
from src.projectiles import Arrow

TILE_SIZE    = 40
SHOOT_LINGER = 600  # ms

_SPRITE_ROOT = Path(__file__).resolve().parents[2] / "assets" / "images" / "towers" / "archer"


def _load_anim_folder(folder):
    folder = Path(folder)
    if not folder.is_dir():
        return []
    files = sorted(f for f in os.listdir(folder) if f.lower().endswith(".png"))
    frames = []
    for filename in files:
        img = pygame.image.load(str(folder / filename)).convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        frames.append(img)
    return frames


class ArcherTower(Tower):
    CRIT_CHANCE = 0.2

    _idle_frames        = None
    _shoot_stand_frames = None

    def __init__(self, position):
        super().__init__(position, cost=100)
        self.damage = 25
        self.attack_range = 150
        self.attack_speed = 1.5

        self.current_frame   = 0
        self.animation_timer = 0
        self.animation_speed = 80  # ms per frame
        self._is_shooting    = False
        self._shoot_end_time = 0
        self.animation_state = "idle"

        if ArcherTower._idle_frames is None:
            ArcherTower._idle_frames        = _load_anim_folder(_SPRITE_ROOT / "Idle")
            ArcherTower._shoot_stand_frames = _load_anim_folder(_SPRITE_ROOT / "Shoot_Stand")

    def _on_attack(self, target, enemies):
        dmg = self.damage
        if random.random() < self.CRIT_CHANCE:
            dmg *= 2
        now = pygame.time.get_ticks()
        if not self._is_shooting:
            self._is_shooting    = True
            self.current_frame   = 0
            self.animation_timer = now
        self._shoot_end_time = now + SHOOT_LINGER
        return Arrow(self.position, target, dmg)

    def draw(self, screen):
        x, y = int(self.position.x), int(self.position.y)
        now = pygame.time.get_ticks()

        # Resolve state
        if self._is_shooting and now > self._shoot_end_time:
            self._is_shooting = False

        new_state = "shoot" if self._is_shooting else "idle"
        if new_state != self.animation_state:
            self.animation_state = new_state
            self.current_frame   = 0
            self.animation_timer = now

        frames = (
            ArcherTower._shoot_stand_frames if self.animation_state == "shoot"
            else ArcherTower._idle_frames
        )

        # Advance frame (looping)
        if frames and now - self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.animation_timer = now

        # Draw sprite or fallback
        if frames and 0 <= self.current_frame < len(frames):
            screen.blit(frames[self.current_frame], (x - TILE_SIZE // 2, y - TILE_SIZE // 2))
        else:
            pygame.draw.ellipse(screen, (22, 38, 24), (x - 18, y + 10, 36, 12))
            pygame.draw.circle(screen, (92, 62, 40), (x, y + 2), 14)
            pygame.draw.circle(screen, (168, 123, 84), (x, y + 2), 14, 2)
            pygame.draw.line(screen, (73, 121, 68), (x, y - 14), (x, y + 14), 4)
            pygame.draw.arc(screen, (165, 228, 148), (x - 11, y - 14, 16, 28), 1.2, 5.1, 3)
            pygame.draw.line(screen, (234, 225, 201), (x - 3, y - 10), (x - 3, y + 10), 2)
            pygame.draw.line(screen, (234, 225, 201), (x + 2, y - 4), (x + 13, y - 10), 2)

        font = pygame.font.SysFont("verdana", 12, bold=True)
        label = font.render(f"Lv{self.level}", True, (255, 255, 255))
        screen.blit(label, (x - label.get_width() // 2, y + TILE_SIZE // 2 + 2))

        mode_surf = font.render(TARGETING_LABELS[self.targeting_mode], True, (255, 220, 80))
        screen.blit(mode_surf, (x - mode_surf.get_width() // 2, y - TILE_SIZE // 2 - mode_surf.get_height() - 1))
