
from pyfiglet import figlet_format

text = input("Digite algo: ")
ascii_art = figlet_format(text, font='roman')  # To set another font, add a parameter 'font'

print(ascii_art)

# References:
# http://www.figlet.org/examples.html
# https://www.youtube.com/watch?v=Y0QiBbI3MWs
