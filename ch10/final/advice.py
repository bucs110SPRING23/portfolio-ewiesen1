import requests

class Advice:
    def __init__(self):
        """
        Initializes the instance variable with the url of the Advice Slip API.
        Args: self
        Return: None
        """
        self.url = "https://api.adviceslip.com/advice"
    def get_advice(self):
        """
        Grabs a random advice quote from the advice slip API.
        Args: self
        Return: advice
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            advice = data["slip"]["advice"]
            return(advice)
        else:
            return("Failed to fetch advice")
    def __str__(self):
        """
        A string representation of the class instance.
        Args: self
        Return: (str) f"Advice(url={'self.url'}" 
        """
        return f"Advice(url={'self.url'}"
 