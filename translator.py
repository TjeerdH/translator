from googletrans import Translator
translator = Translator()
my_file = open("../../Desktop/Python/text.txt", "r")
contents = my_file.read()
translated_contents = str(translator.translate(contents, src="en", dest="ja"))
new_file = open("../../Desktop/Python/translated.txt", "w")
new_file.write(translated_contents)

print(translated_contents)