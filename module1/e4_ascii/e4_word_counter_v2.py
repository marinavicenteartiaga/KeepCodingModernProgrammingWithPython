my_text = "En   un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de " \
          "os de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca " \
          "que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, " \
          "algún palomino de añadidura los domingos8, consumían las tres partes de su hacienda. " \
          "El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos " \
          "de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama " \
          "que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así " \
          "ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años. " \
          "Era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. " \
          "Quieren decir que tenía el sobrenombre de «Quijada», o «Quesada», que en esto hay alguna diferencia en " \
          "los autores que deste caso escriben, aunque por conjeturas verisímilesII se deja entender que " \
          "se llamaba «Quijana». Pero esto importa poco a nuestro cuento: basta que en la narración dél " \
          "no se salga un punto de la verdad."

num_words = 0
position = 0
previous_char = " "

for character in my_text:
    if character == " " and previous_char != " ":
        num_words += 1
    previous_char = character

if character != " ":
    num_words += 1

print("Total number of words: ", num_words)

...
while position < len(my_text):
    if my_text[position] == " " and my_text[position - 1] != " ":
        num_words += 1
    position += 1

if my_text[position - 1] != " ":
    num_words += 1
...

