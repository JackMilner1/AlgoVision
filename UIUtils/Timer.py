from pygame.time import get_ticks
import pygame

class Timer:
    # get_ticks() returns the point in time your at from when the application was lauched

    def __init__(self,duration):
        self.duration = duration * 1000
        self.startTime = 0 # point in time timer started
        self.timeElapsed = 0 # the amount of time the timer has been on for
        self.active = False # whether the timer currently paused
        self.pauseTicks = 0 # time elapsed since timer was paused 
        self.paused = False
        self.timeRanOut = False

    def start(self):
        self.active = True
        self.startTime = get_ticks()

    def timeout(self):
        self.timeRanOut = True
        self.active = False
        self.startTime = 0

    def pause(self):
        if not self.paused:
            self.active = False
            self.paused = True
            self.pauseTicks = get_ticks() # point in time the timer stops from when the application was lauched

    def unpause(self):
        # resets start time as the pausing of the timer messes up the get ticks function
        # this is because the get_ticks function is based on when the app was launched not the actual amount of time passed in the timer
        if self.paused:
            self.paused = False
            newTicks = get_ticks()
            self.startTime = self.startTime + (newTicks - self.pauseTicks) 
            self.active = True

    def update(self):
        if self.active:
            currentTime = get_ticks()
            self.timeElapsed = currentTime - self.startTime # finds the time passed by the timer
            if self.timeElapsed >= self.duration:
                self.timeout() # clock has ran out of time

    def time(self):
        time = (self.duration // 1000) - (self.timeElapsed // 1000)
        return time // 60, time % 60
    
    def reset(self,duration):
        self.duration = duration * 1000
        self.startTime = 0 # point in time timer started
        self.timeElapsed = 0 # the amount of time the timer has been on for
        self.active = False # whether the timer currently paused
        self.pauseTicks = 0 # time elapsed since timer was paused 
        self.timeRanOut = False
        self.start()

    def drawTimerUI(self,screen, x, y, height, width):


        minutes,seconds = self.time() 

        color = (253, 255, 255)
        
        rect = pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
 
        font = pygame.font.Font('freesansbold.ttf', 32)

        minutes = str(minutes)
        seconds = str(seconds)

        if len(seconds) == 1:
            if seconds == "0":
                seconds = "00"
            else:
                seconds = "0" + seconds
 
        text = font.render(str(minutes) + ":" + str(seconds), True , (200,200,200))

        textRect = text.get_rect()
        
        textRect.center = rect.center

        screen.blit(text, textRect)