import os, sys

class Input:
	def __init__(self):
		pass
	
	def text(text: str)-> None: 
		os.system(f'input text {text}')
	
	def keyevent(key_code: str)-> None:
		os.system(f'input keyevent {key_code}')
	
	def tap(x: str, y: str)-> None:
		os.system(f'input tap {x} {y}')
	
	def swipe(x1, y1, x2, y2, duration):
		os.system(f'input swipe {x1} {y1} {x2} {y2} {duration}')
	
	def draganddrop(x1: str, y1: str, x2: str, y2: str, duration: str)-> None:
		os.system(f'input draganddrop {x1} {y1} {x2} {y2} {duration}')
	
	def press():
		pass
	
	def  roll(dx: str, dy: str)-> None:
		os.system(f'input roll {dx} {dy}')



class Screen:
	def cap(save_cap_path):
		os.system(f'screencap {save_cap_path}')
	
	def record(save_record_path):
		os.system(f'screenrecord {save_record_path}')
