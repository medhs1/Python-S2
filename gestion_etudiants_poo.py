class etudiant:
    """
    Classe représentant un étudiant et ses données académiques.
    
    Attributes:
        idEtud (str): L'identifiant unique de l'étudiant (ex: code Massar).
        nomEtud (str): Le nom de famille ou complet de l'étudiant.
        gpaEtud (float): La moyenne générale de l'étudiant.
        __ageEtd(int): L'age de l'étudiant.
    """

    def __init__(self, id, nom, age, gpa):
        """
        Initialise une nouvelle instance de la classe etudiant.

        Args:
            id (str): L'identifiant unique ou code Massar de l'étudiant.
            nom (str): Le nom de l'étudiant.
            age (int): L'âge de l'étudiant (sera stocké comme attribut privé).
            gpa (float): La moyenne générale (GPA) de l'étudiant.
        """
        self.idEtud = id
        self.nomEtud = nom
        self.__ageEtud = age  # Attribut privé
        self.gpaEtud = gpa

    def getAge(self):
        """
        Permet d'accéder à l'âge de l'étudiant (Getter / Accesseur).

        Returns:
            int: L'âge privé de l'étudiant.
        """
        return self.__ageEtud

    def setAge(self, age):
        """
        Permet de modifier l'âge de l'étudiant avec une validation de sécurité (Setter).
        
        L'âge fourni doit être compris dans un intervalle réaliste (entre 1 et 119 ans inclus).
        Si la valeur est incorrecte, un message d'erreur est affiché et l'attribut n'est pas modifié.

        Args:
            age (int): Le nouvel âge à appliquer à l'étudiant.

        Returns:
            None
        """
        if age > 0 and age < 120:
            self.__ageEtud = age
        else:
            print("L'age n'est pas valid")

# Création des instances (objets)
etudiant1 = etudiant("B13273405", "Mohamed", 19, 15.94)
etudiant2 = etudiant("M24404759", "Omar", 20, 15.23)
etudiant3 = etudiant("A38032836", "Nora", 18, 19.55)
etudiant4 = etudiant("M21937940", "Laila", 19, 13.81)


def printer():
    """
    Regroupe les étudiants instanciés dans une liste locale, la parcourt,
    puis affiche la carte d'identité textuelle de chaque étudiant.

    Returns:
        None
    """
    liste_etudiants = [etudiant1, etudiant2, etudiant3, etudiant4]
    for etd in liste_etudiants:
        print(f"Bonjour {etd.nomEtud}, votre Massar est: {etd.idEtud}, tu as {etd.getAge()} ans, votre moyenne est: {etd.gpaEtud}")
        print("-" *85)

printer()