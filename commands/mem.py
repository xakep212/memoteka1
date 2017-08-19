import command_system
import vkapi


def mem():
   attachment = vkapi.get_random_wall_picture(-32015300)
   message = 'Держи рандомный мем со стены\nВ следующий раз я пришлю другой.'
   return message, attachment

mem_command = command_system.Command()

mem_command.keys = ['мем', 'мемас', 'мемес', 'ор', 'meme', 'memes']
mem_command.description = 'Пришлю картинку с memesом'
mem_command.process = mem
