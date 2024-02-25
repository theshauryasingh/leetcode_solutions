class TextEditor:
    def __init__(self):
        self.currentText = ""
        self.cursorPosition = 0

    def addText(self, text: str) -> None:
        temp = self.currentText[self.cursorPosition:]
        self.currentText = self.currentText[:self.cursorPosition] + text
        self.currentText = self.currentText + temp
        self.cursorPosition += len(text)
        # print(self.cursorPosition, self.currentText)
        
    def deleteText(self, k: int) -> int:
        temp = self.currentText[self.cursorPosition:]
        delete = k
        if len(self.currentText[:self.cursorPosition]) < k:
            delete = len(self.currentText[:self.cursorPosition])
        self.currentText = self.currentText[:self.cursorPosition][: -1*k]
        self.currentText = self.currentText + temp
        self.cursorPosition -= k
        if not 0 <= self.cursorPosition:
            self.cursorPosition = 0
        return delete

    def cursorLeft(self, k: int) -> str:
        self.cursorPosition -= k
        if not 0 <= self.cursorPosition:
            self.cursorPosition = 0
        # print(k, self.cursorPosition)
        return self.currentText[:self.cursorPosition][-1 * min(10, self.cursorPosition):]

    def cursorRight(self, k: int) -> str:
        self.cursorPosition += k
        if not self.cursorPosition <= len(self.currentText):
            self.cursorPosition = len(self.currentText)
        # print(k, self.cursorPosition)
        return self.currentText[:self.cursorPosition][-1 * min(10, self.cursorPosition):]

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)