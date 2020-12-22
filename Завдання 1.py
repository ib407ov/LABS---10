# cтворити змінну для тексту та назву теми
#
# визначити кількість букв тексту
# визначити кількість пробілів
# заміни кожного входження однієї букви на іншу;
# видалення слова за номером

class Text:
    def __init__(self, _nameText, _text):
        self.nameText = _nameText
        self.Text = _text

    @property
    def howLettersInText(self):
        return (len(self.Text))

    @property
    def howManySpaces(self):
        a = 0
        for i in range(g.howLettersInText):
            if self.Text[i] == ' ':
                a += 1
        return a

    @property
    def secretText(self):
        l = 0
        A = []
        for i in range(self.howLettersInText):
            A.append(ord(self.Text[i]))
        return print('secret = ', A)

    def deleteWord(self, numberWord):
        A = self.Text.split()
        print('You delete word : ', A[numberWord])
        del A[numberWord]
        return A

yN = input('you have write text? (y/n) : ')
if yN == 'y':
    a = input('Name text : ')
    b = input('writte : ')
    g = Text(a, b)
else:
    g= Text('EPIGRATH','Learn everything you need to know')
#----------1
print(g.howLettersInText)
#----------2
print(g.howManySpaces)
#----------3
print(g.secretText)
#----------4
yN = input('Do you have delete word? (y/n) : ')
if yN == 'y':
    a = int(input('delete word = '))
    print(g.deleteWord(a))