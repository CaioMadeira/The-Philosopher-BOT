import random, os, textwrap
from Lists.img_list import PHILOSOPHERS_LIST
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH
from PIL import Image, ImageDraw, ImageFont


emojis_quotes = ["Oi, tudo bem.", "Oi", "Tudo bien \u2713"]


img = Image.open(f'{TEMPLATES_PATH}/layer_1.png')
font = ImageFont.truetype(r'C:\Users\caiom\Documents\GitHub\The-Philosopher-BOT\Font\myriad.otf', 50)
drawing = ImageDraw.Draw(img)

choice_philosopher = random.choice(PHILOSOPHERS_LIST)
remove_path_of_filename = os.path.basename(choice_philosopher)
print(f"Imagem do filósofo escolhida: {remove_path_of_filename}")

remove_extension_of_filename = remove_path_of_filename.replace('.png', '')
if f'({int})' in remove_extension_of_filename:
    print("Removendo lixo no nome da imagem do filosofo...")
    remove_number_in_name = remove_extension_of_filename.replace('(2)', '')
    finish_name_of_philosopher = f'- {remove_number_in_name}'
    print(f'Nome do filósofo tratado: {finish_name_of_philosopher}')
else:
    finish_name_of_philosopher = f'- {remove_extension_of_filename}'
    print("Nenhum lixo no nome da imagem encontrado. Prosseguindo normalmente...")
    print(f'Nome do filósofo tratado: {finish_name_of_philosopher}')

philosopher_str_to_obj = Image.open(choice_philosopher)
img_2 = philosopher_str_to_obj.resize((449, 584))
img.paste(img_2, (629, 0))
smooth_template = Image.open(f'{TEMPLATES_PATH}/layer_3.png')
img.paste(smooth_template, (0, 0), smooth_template)
TEXTO = drawing.text(xy=(60, 128), text=textwrap.fill(str(random.choice(emojis_quotes)), 20), fill=(255, 255, 255), font=font)
font = ImageFont.truetype("Font/times.ttf", 30)
drawing.text(xy=(43, 512),
             text=textwrap.fill(str(finish_name_of_philosopher), 25),
             fill=(255, 255, 255),
             font=font)
img.save('emoji_teste.png')
img.show()
print("Sucesso!")