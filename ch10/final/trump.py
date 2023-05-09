import requests
   
class DTJoke:
    def __init__(self):
        """
        Initializes the instance variable with the url of the Tronald Dump API.
        Args: self
        Return: None
        """
        self.url = "https://api.tronalddump.io/random/quote"
    def get_joke(self):
        """
        Grabs a random advice quote from the Tronald Dump API.
        Args: self
        Return: quote
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            quote = data["value"]
            return(quote)
        else:
            return("Failed to fetch quote")
    def __str__(self):
        """
        A string representation of the class instance.
        Args: self
        Return: (str) f"DTJoke(url={'self.url'})" 
        """
        return f"DTJoke(url={'self.url'})"