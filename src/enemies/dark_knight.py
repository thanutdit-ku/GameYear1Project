from pathlib import Path

import pygame
from src.enemies.enemy import Enemy

_ASSET_DIR  = Path(__file__).resolve().parents[2] / "assets" / "images" / "enemies" / "dark_knight" / "FreeKnight"
_FRAME_W    = 120
_FRAME_H    = 80
_DISPLAY_W  = 72
_DISPLAY_H  = 48
_ANIM_SPEED = 100  # ms per frame


def _slice_sheet(filename, num_frames):
    sheet = pygame.image.load(str(_ASSET_DIR / filename)).convert_alpha()
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface(pygame.Rect(i * _FRAME_W, 0, _FRAME_W, _FRAME_H))
        frames.append(pygame.transform.smoothscale(frame, (_DISPLAY_W, _DISPLAY_H)))
    return frames


class DarkKnight(Enemy):
    _run_frames   = None
    _idle_frames  = None
    _death_frames = None

    def __init__(self, waypoints):
        super().__init__(waypoints)
        self.hp          = 300
        self.max_hp      = 300
        self.speed       = 42
        self.reward_gold = 50

        self._death_frame   = 0
        self._death_done    = False
        self._death_timer   = 0

        if DarkKnight._run_frames is None:
            DarkKnight._run_frames   = _slice_sheet("_Run.png",   10)
            DarkKnight._idle_frames  = _slice_sheet("_Idle.png",  10)
            DarkKnight._death_frames = _slice_sheet("_Death.png", 10)

    def draw(self, screen):
        x, y = int(self.position.x), int(self.position.y)
        now  = pygame.time.get_ticks()

        if self.is_dead():
            # Play death animation once
            if not self._death_done:
                if now - self._death_timer >= _ANIM_SPEED:
                    self._death_frame += 1
                    self._death_timer  = now
                if self._death_frame >= len(self._death_frames):
                    self._death_done = True
                    return
            else:
                return
            frame = self._death_frames[min(self._death_frame, len(self._death_frames) - 1)]
        else:
            # Walk animation while alive
            idx   = (now // _ANIM_SPEED) % len(self._run_frames)
            frame = self._run_frames[idx]

        rect = frame.get_rect(center=(x, y))
        screen.blit(frame, rect)
        self._draw_health_bar(screen, x, rect.top + 4, 60, -16, color=(225, 130, 130))
