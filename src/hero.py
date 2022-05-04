import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.speed = 3
        self.health = 3
        """
	description: initialize the hero, creates object of enemy
	args: pygame.sprite, sprite
	return: none
	"""
    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

        """
	description: makes speed quicker as they go in one direction continously
	args: self
	return: none
	"""


    def fight(self, opponent):
      if(random.randrange(3)):
        story1 = input("The enemy says,""I got you!"". Before it strikes, you however, are a witch, and can maybe cast a spell to save yourself. Type a spell that might save you!.")
        if len(story1) >= 10:
          print("Hazzah! Your spell was enough!")
          return True
        elif len(story1) % 2 == 0:
          print("Hazzah! Your spell was so powerful that it gave you another life!")
          self.health += 1
          return True
        elif len(story1) <= 5:
          print("You failed! Maybe you can get another life by being EVEN better.")
          print("attack failed. Remaining Health: ", self.health)
          return False
      else:
        print("successful attack")
        return True
      
        """
	description: initialize the enemy, creates object of enemy and allows the fight option
	args: self,opponent
	return: False, True
	"""