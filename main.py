# -*- coding: utf-8 -*-


#в целом что-то сложное встречается только в классах человека и группы, а в других - просто сборка функций



import group_bot
import vk_bot

def main():
	group_token = '3e43264dcb39c26b2b9f86902c878f12897ba0b842331eb9340f6d0315d119f6e8095093de2b802d78432'#group mrb
	bot_token   = 'e84a6420bbde0273488e16dea2228699a620ded0c9504f0945c91e4c4cebaac2848bb464edea2ce1e1c9e'#bot

	bot = vk_bot.bot(bot_token)#инициализируем обьекты с нашими токенами
	group = group_bot.group(group_token,174145768)
	group.get_group_members(group.id)

	bot.add_friends(12, bot.get_rand_ids(12))
	#тут основное место для ваших злых деяний


if __name__ == '__main__':
	main()

