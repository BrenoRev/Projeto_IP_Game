import cv2
import pygame

class Video:
    def play(self):

        # Tocar música de introdução star wars
        musica_introducao = pygame.mixer.music.load('musics/Star_Wars.mp3')
        pygame.mixer.music.play(-1)

        video = cv2.VideoCapture("Video/Introduction.mp4")
        success, video_image = video.read()
        fps = video.get(cv2.CAP_PROP_FPS)

        window = pygame.display.set_mode(video_image.shape[1::-1])
        clock = pygame.time.Clock()

        run = success
        while run:

            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            success, video_image = video.read()
            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
            else:
                run = False
            window.blit(video_surf, (0, 0))
            pygame.display.flip()

        # Stop musics
        pygame.mixer.music.stop()