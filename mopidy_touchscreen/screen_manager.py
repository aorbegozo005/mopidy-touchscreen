from .main_screen import MainScreen
import pygame
import logging

logger = logging.getLogger(__name__)

class ScreenManager():

	

	def __init__(self,size):
		self.screen_size=size
		self.screens=[MainScreen(size,self,"/home/ander")]
		self.track=None

	def update(self,core):
		return self.screens[0].update(core)

	def track_started(self,track):
		self.track=track
		self.screens[0].track_started(track.track)

