class StringUtility:
    def __init__(self,string):
        self.string = string
        
    def __str__(self):
        return self.string

    def vowels(self):
        vowels = 0
        for v in self.string:
            if v in "aeiou":
                vowels += 1
        if vowels >= 5:
            vowels = "many"
        return str(vowels)
    
    def bothEnds(self): 
        if len(self.string) > 2:
            return f"{self.string[0]}{self.string[1]}{self.string[-2]}{self.string[-1]}"

        else:
            return ""
    
    def fixStart(self):
        replaced = ""
        for star in self.string:
            if star == self.string[0] and replaced != "":
                replaced += "*"
            else:
                replaced += star
        return replaced

    def asciiSum(self):
        sum = 0
        for ch in self.string:
            sum += (ord(ch)) #converts char into int
        return sum
    
    def cipher(self):
        result = ""
        for char in self.string:
            shift = len(self.string)
            if char.isalpha():
                # Determine the case of the character
                start = ord('A') if char.isupper() else ord('a')
                # Calculate the new position of the character after the shift
                new_pos = (ord(char) - start + shift) % 26
                # Convert the new position back to a character
                char = chr(start + new_pos)
            result += char
        return result

        